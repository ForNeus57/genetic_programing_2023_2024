from __future__ import annotations

from math import ceil, sqrt
from dataclasses import dataclass

from src.genetic.individual.individual import Individual
from src.genetic.individual.structure.metadata import Metadata, GenerationMethod


@dataclass(slots=True)
class Population:
    individuals: list[Individual]

    @classmethod
    def from_ramped_half_and_half(cls, size: int) -> Population:
        population: list[Individual] = []

        for i in range(1, int(ceil(sqrt(size * 2)))):
            if i % 2 == 0:
                method: GenerationMethod = GenerationMethod.GROW
            else:
                method: GenerationMethod = GenerationMethod.FULL

            for _ in range(i):
                ind: Individual = Individual.from_random(Metadata(method=method))
                population.append(ind)

        return cls(population)

