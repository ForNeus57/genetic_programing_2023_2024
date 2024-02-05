from __future__ import annotations

from dataclasses import dataclass, field
from multiprocessing import Pool
from time import perf_counter
from typing import Callable, TypeVar, ClassVar
from random import random

from src.genetic.evaluation.evaluation import FitnessFunctionBase
from src.genetic.evolution.population import Population
from src.genetic.evolution.statistics import Statistics
from src.genetic.individual.individual import Individual

T = TypeVar('T', float, int)


@dataclass(slots=True)
class Evolution:
    fitness_grader: FitnessFunctionBase
    input_vector: list[tuple[int | bool]]
    generations: int = 100
    process_pool_number: int = 10

    fitness: tuple = field(init=False)
    statistics: Statistics = field(init=False)
    population: Population = field(init=False)

    crossover_probability: ClassVar[float] = 0.9

    def __post_init__(self):
        self.statistics = Statistics()
        start = perf_counter()
        self.population = Population.from_ramped_half_and_half(50)
        print(perf_counter() - start)

        with Pool(self.process_pool_number) as pool:
            self.fitness = tuple(
                pool.map(
                    Evolution.calculate_fitness,
                    map(lambda x: (x, self.input_vector, self.fitness_grader), self.population.individuals),
                )
            )

        self.statistics.add_new_snapshot(self.population, self.fitness)
        print(self.fitness)

    def evolve(self, epsilon: float | int = 0) -> bool:

        for _ in range(1, self.generations):
            if self.statistics.finished(epsilon):
                return True

            for index in range(len(self.population.individuals)):

                if random() < Evolution.crossover_probability:
                    pass
                else:
                    pass

        return False

    @staticmethod
    def calculate_fitness(x: tuple[Individual, list[tuple], FitnessFunctionBase]) -> T:
        ind, input_vector, fitness_function = x
        return sum(ind.evaluate(fitness_function, i_v) for i_v in input_vector)
