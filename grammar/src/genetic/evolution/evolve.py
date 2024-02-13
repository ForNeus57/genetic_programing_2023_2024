from __future__ import annotations

import os
import shutil
from copy import deepcopy
from dataclasses import dataclass, field
from math import ceil
from multiprocessing import Pool
from pathlib import Path
from random import random, sample, getstate
from time import perf_counter
from typing import ClassVar, Optional

from src.genetic.evaluation.evaluation import FitnessFunctionBase
from src.genetic.evolution.population import Population
from src.genetic.individual.individual import Individual
from src.genetic.individual.structure.metadata import GenerationMethod, Metadata


@dataclass(slots=True)
class Evolution:
    fitness_grader: FitnessFunctionBase
    input_vector: list[Optional[tuple]]

    fitness: list = field(init=False)
    statistics: Statistics = field(init=False)
    population: Population = field(init=False)

    generations: ClassVar[int] = 200
    crossover_probability: ClassVar[float] = 0.2
    pool_size: ClassVar[int] = os.cpu_count()

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

        # with Pool(processes=Evolution.pool_size) a:
        self.fitness = list(
            map(
                lambda x: self.calculate_fitness(x),
                iter(self.population),
            )
        )

        self.statistics.add_new_snapshot(self.population, self.fitness)

    def evolve(self, epsilon: float | int = 0) -> bool:
        # with Pool(processes=Evolution.pool_size) as pool:
        for _ in range(1, Evolution.generations):
            if self.statistics.finished(epsilon):
                self.population.save_to_pickle(
                    Path(self.statistics.save_directory + 'final_population')
                )
                return True

            for _ in range(len(self.population)):
                fitness_join_individuals: tuple = tuple(enumerate(zip(self.fitness, iter(self.population))))
                _, (_, first) = deepcopy(Individual.tournament(
                    sample(fitness_join_individuals, max(1, ceil(0.1 * len(self.population)))),
                    'min'
                ))
                if random() < Evolution.crossover_probability:
                    _, (_, second) = deepcopy(Individual.tournament(
                        sample(fitness_join_individuals, max(1, ceil(0.1 * len(self.population)))),
                        'min'
                    ))
                    first.crossover(second)
                else:
                    first.mutate()

                index_to_change = deepcopy(Individual.tournament(
                    sample(fitness_join_individuals, max(1, ceil(0.1 * len(self.population)))),
                    'max'
                ))[0]

                self.fitness[index_to_change] = self.calculate_fitness(first)

                self.population[index_to_change] = first

            for _ in range(ceil(len(self.population) * 0.2)):
                fitness_join_individuals: tuple = tuple(enumerate(zip(self.fitness, iter(self.population))))
                index_to_change = deepcopy(Individual.tournament(
                    list(fitness_join_individuals),
                    'max'
                ))[0]
                new_offspring: Individual = Individual.from_random(Metadata(
                    method=(
                        GenerationMethod.GROW if random() < 0.5 else GenerationMethod.FULL
                    )
                ))

                new_fitness: int = self.calculate_fitness(new_offspring)
                self.fitness[index_to_change] = new_fitness
                self.population[index_to_change] = new_offspring

            self.statistics.add_new_snapshot(self.population, self.fitness)

        self.population.save_to_pickle(
            Path(self.statistics.save_directory + 'final_population')
        )
        return False

    def calculate_fitness(self, ind: Individual) -> int | float:
        print('.', end='')
        return sum(map(ind.evaluate, map(lambda y: (self.fitness_grader, y), self.input_vector)))


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
                               f'Mutation probability: {1. - Evolution.crossover_probability}')

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

        # print(fitness_vector)
        for individual, fitness in zip(iter(population), fitness_vector):
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
        print('\n')
        print(point)
        # print(Interpreter.interpret(
        #     str(best[1]),
        #     BufferInputOutputOperation(
        #
        #     )
        # ).output)
        self.prev = perf_counter()
        self.save_to_directory(best[1])

    def finished(self, epsilon: float | int) -> bool:
        if condition := self.history[-1].best <= epsilon:
            with open(self.save_directory + 'status.txt', 'a') as file:
                file.write('Finished!')
        return condition

    def save_to_directory(self, best_program: Individual) -> None:
        with open(self.save_directory + 'history.txt', 'a') as file:
            file.write(str(self.history[len(self.history) - 1]))

        best_program.save_to_file(Path(self.save_directory + f'best_program{len(self.history) - 1}.pkl'))
