from __future__ import annotations

from dataclasses import dataclass
from itertools import chain
from math import ceil, sqrt
from multiprocessing import Pool
from typing import Iterable

from src.genetic.individual.individual import Individual
from src.genetic.individual.structure.metadata import Metadata, GenerationMethod


@dataclass(slots=True)
class Population:
    individuals: tuple[Individual, ...]

    @classmethod
    def from_ramped_half_and_half(cls, size: int) -> Population:
        def get_method_by_index(index: int) -> Iterable[GenerationMethod]:
            method: GenerationMethod = GenerationMethod.GROW if index % 2 == 0 else GenerationMethod.FULL
            return (method for _ in range(index))

        population: map = map(get_method_by_index, range(1, ceil(sqrt(size * 2))))

        with Pool(10) as pool:
            individuals: list[Individual] = pool.map(Population.construct_individuals, chain.from_iterable(population))

            return cls(tuple(individuals))

    @staticmethod
    def construct_individuals(method: GenerationMethod) -> Individual:
        return Individual.from_random(Metadata(method=method))
