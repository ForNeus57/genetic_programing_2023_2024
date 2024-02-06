from __future__ import annotations

from dataclasses import dataclass
from itertools import chain
from math import ceil, sqrt
from typing import Iterable, ClassVar

from src.genetic.individual.individual import Individual
from src.genetic.individual.structure.metadata import Metadata, GenerationMethod


@dataclass(slots=True)
class Population:
    individuals: list[Individual]
    # pool_size: ClassVar[int] = 10

    default_population_size: ClassVar[int] = 100

    @classmethod
    def from_ramped_half_and_half(cls, size: int = default_population_size) -> Population:
        def get_method_by_index(index: int) -> Iterable[GenerationMethod]:
            method: GenerationMethod = GenerationMethod.GROW if index % 2 == 0 else GenerationMethod.FULL
            return (method for _ in range(index))

        population: map = map(get_method_by_index, range(1, ceil(sqrt(size * 2))))

        # with Pool(Population.pool_size) as pool:
        #     individuals: list[Individual] = pool.map(Population.construct_individuals, chain.from_iterable(population),
        #                                              chunksize=(size // Population.pool_size) + 1)
        individuals: Iterable[Individual] = map(lambda x: Individual.from_random(Metadata(method=x)), chain.from_iterable(population))

        return cls(list(individuals))

    def __len__(self):
        return len(self.individuals)