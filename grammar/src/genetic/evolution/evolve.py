from __future__ import annotations

import os
import shutil
from copy import deepcopy
from dataclasses import dataclass, field
from math import ceil
from pathlib import Path
from random import random, sample, getstate
from time import perf_counter
from typing import TypeVar, ClassVar

from src.genetic.evaluation.evaluation import FitnessFunctionBase
from src.genetic.evolution.population import Population
from src.genetic.individual.individual import Individual
from src.genetic.interpreter.input_output import BufferInputOutputOperation
from src.genetic.interpreter.interpreter import Interpreter

T = TypeVar('T', float, int)


@dataclass(slots=True)
class Evolution:
    fitness_grader: FitnessFunctionBase
    input_vector: list[tuple[int | bool]]

    fitness: list = field(init=False)
    statistics: Statistics = field(init=False)
    population: Population = field(init=False)

    generations: ClassVar[int] = 100
    crossover_probability: ClassVar[float] = 0.5

    def __post_init__(self):
        name: str = self.fitness_grader.__class__.__name__

        self.statistics = Statistics(
            save_directory=f'./data/python/{
                name[
                    next((index for index, char in enumerate(name) if char.isdigit()), -1):
                ]
            }/'
        )
        self.population = Population.from_ramped_half_and_half()

        # with Pool(Evolution.process_pool_number) as pool:
        self.fitness = list(
            map(
                Evolution.calculate_fitness,
                map(lambda x: (x, self.input_vector, self.fitness_grader), self.population.individuals),
            )
        )

        self.statistics.add_new_snapshot(self.population, self.fitness)

    def evolve(self, epsilon: float | int = 0) -> bool:
        for _ in range(1, Evolution.generations):
            if self.statistics.finished(epsilon):
                return True

            for _ in range(len(self.population)):
                fitness_join_individuals: tuple = tuple(enumerate(zip(self.fitness, self.population.individuals)))
                _, (_, first) = deepcopy(Individual.tournament(
                    sample(fitness_join_individuals, max(1, ceil(0.2 * len(self.population)))),
                    'min'
                ))
                if random() < Evolution.crossover_probability:
                    _, (_, second) = deepcopy(Individual.tournament(
                        sample(fitness_join_individuals, max(1, ceil(0.2 * len(self.population)))),
                        'min'
                    ))
                    first.crossover(second)
                else:
                    first.mutate()

                index_to_change = deepcopy(Individual.tournament(
                    sample(fitness_join_individuals, max(1, ceil(0.2 * len(self.population)))),
                    'max'
                ))[0]

                self.fitness[index_to_change] = Evolution.calculate_fitness(
                    (first, self.input_vector, self.fitness_grader)
                )

                self.population.individuals[index_to_change] = first

            self.statistics.add_new_snapshot(self.population, self.fitness)

        return False

    @staticmethod
    def calculate_fitness(x: tuple[Individual, list[tuple], FitnessFunctionBase]) -> T:
        ind, input_vector, fitness_function = x
        return sum(ind.evaluate(fitness_function, i_v) for i_v in input_vector)


@dataclass(slots=True)
class HistoryPoint:
    generation_number: int = 0
    best: float = field(default=float('inf'))
    worst: float = field(default=float('-inf'))
    average: float = 0.
    best_program: str = ''
    elapsed_time: float = 0.

    def __str__(self) -> str:
        return f'[{self.generation_number}]Best: {self.best}, Worst: {self.worst}, Average: {self.average}' \
               f', Time: {self.elapsed_time}\nBest program: {self.best_program}\n'


@dataclass(slots=True)
class Statistics:
    history: list[HistoryPoint] = field(default_factory=list, init=False)
    prev: float = perf_counter()
    save_directory: str = ''

    def __post_init__(self):
        config_details: str = (f'Configuration:\n'
                               f'Save directory: {Path(self.save_directory).absolute()}\n'
                               f'Seed: {getstate()[1][0]}\n'
                               f'Generations: {Evolution.generations}\n'
                               f'Population size: {Population.default_population_size}\n'
                               f'Crossover probability: {Evolution.crossover_probability}\n'
                               f'Mutation probability: {1 - Evolution.crossover_probability}\n')

        if os.path.exists(self.save_directory):
            shutil.rmtree(self.save_directory)
        Path(self.save_directory).mkdir(parents=True, exist_ok=True)
        with open(self.save_directory + 'status.txt', 'w') as file:
            file.write(
                config_details
            )
            print(config_details)

    def add_new_snapshot(self, population: Population, fitness_vector: list) -> None:
        best = (float('inf'), None)
        worst = float('-inf')

        print(fitness_vector)
        for individual, fitness in zip(population.individuals, fitness_vector):
            if fitness < best[0]:
                best = fitness, individual
            if fitness > worst:
                worst = fitness

        point = HistoryPoint(
            len(self.history),
            best[0],
            worst,
            sum(fitness_vector) / len(fitness_vector),
            str(best[1]),
            perf_counter() - self.prev
        )

        self.history.append(point)
        print(point)
        print(Interpreter.interpret(
            str(best[1]),
            BufferInputOutputOperation(

            )
        ).output)
        self.prev = perf_counter()
        self.save_to_directory(best[1])

    def finished(self, epsilon: float | int) -> bool:
        if condition := self.history[-1].best <= epsilon:
            with open(self.save_directory + 'status.txt', 'a') as file:
                file.write('Finished!')
        return condition

    def save_to_directory(self, best_program: Individual) -> None:
        with open(self.save_directory + 'history.txt', 'a') as file:
            file.write('\n'.join(map(str, self.history)))

        best_program.save_to_file(self.save_directory + f'best_program{len(self.history)}.pkl')
