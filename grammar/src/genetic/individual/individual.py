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
        pass

    def execute(self, *args, **kwargs) -> tuple:
        pass

    def evaluate(self, *args, **kwargs) -> float:
        pass

    def mutate(self) -> Individual:
        pass

    def crossover(self, other: Individual) -> Individual:
        if isinstance(other, Individual):
            crossover_program: Program = self.program.crossover(other.program)
            return Individual(crossover_program)

        raise TypeError(f"Cannot crossover with {type(other)}.")

    def save_to_file(self, path: str):
        pass
