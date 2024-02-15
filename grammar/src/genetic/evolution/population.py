from __future__ import annotations

from dataclasses import dataclass
from itertools import chain
from math import ceil, sqrt
from pathlib import Path
from typing import Iterable, ClassVar

from src.genetic.individual.individual import Individual
from src.genetic.individual.structure.metadata import Metadata, GenerationMethod


@dataclass(slots=True)
class Population:
    individuals: list[Individual]

    default_population_size: ClassVar[int] = 5_000

    @classmethod
    def from_ramped_half_and_half(cls, size: int = default_population_size) -> Population:
        def get_method_by_index(index: int) -> Iterable[GenerationMethod]:
            method: GenerationMethod = GenerationMethod.GROW if index % 2 == 0 else GenerationMethod.FULL
            return (method for _ in range(index))

        population: map = map(get_method_by_index, range(1, ceil(sqrt(size * 2))))

        individuals: Iterable[Individual] = map(lambda x: Individual.from_random(Metadata(method=x)),
                                                chain.from_iterable(population))

        return cls(list(individuals))

    @classmethod
    def from_pickle(cls, directory: Path) -> Population:
        individuals: Iterable[Individual] = map(Individual.from_file, directory.iterdir())
        return cls(list(individuals))

    def __len__(self) -> int:
        return len(self.individuals)

    def __iter__(self) -> Iterable[Individual]:
        return iter(self.individuals)

    def __getitem__(self, item: int) -> Individual:
        return self.individuals[item]

    def __setitem__(self, key: int, value: Individual) -> None:
        self.individuals[key] = value

    def save_to_pickle(self, directory: Path) -> None:
        directory.mkdir(exist_ok=True)
        for index, individual in enumerate(self.individuals):
            individual.save_to_file(directory.joinpath(f'{index}.pkl'))

    def tournament(self) -> int:
        pass
