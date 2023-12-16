from __future__ import annotations
from dataclasses import dataclass

from src.genetic.individual.structure.program import Program


@dataclass(slots=True, frozen=True, order=False)
class Individual:
    program: Program

    @classmethod
    def from_file(cls, path: str) -> Individual:
        pass

    @classmethod
    def from_random(cls, max_size: int) -> Individual:
        pass

    def __str__(self) -> str:
        raise NotImplementedError()

    def execute(self, *args, **kwargs) -> tuple:
        raise NotImplementedError()

    def evaluate(self, *args, **kwargs) -> float:
        raise NotImplementedError()

    def mutate(self) -> Individual:
        raise NotImplementedError()

    def crossover(self, other: Individual) -> Individual:
        raise NotImplementedError()

    def save_to_file(self, path: str):
        raise NotImplementedError()
