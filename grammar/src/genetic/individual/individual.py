from __future__ import annotations
from dataclasses import dataclass
from pickle import dump, load

from genetic.individual.structure.rules import Program


@dataclass(slots=True, frozen=True, order=False)
class Individual:
    program: Program

    @classmethod
    def from_file(cls, path: str) -> Individual:
        with open(path, 'rb') as file:
            return load(file)

    @classmethod
    def from_random(cls) -> Individual:
        program: Program = Program.from_random()
        return cls(program)

    def __str__(self) -> str:
        return str(self.program)

    def execute(self, *args, **kwargs) -> tuple:
        raise NotImplementedError()

    def evaluate(self, *args, **kwargs) -> float:
        raise NotImplementedError()

    def mutate(self) -> Individual:
        raise NotImplementedError()

    def crossover(self, other: Individual) -> Individual:
        raise NotImplementedError()

    def save_to_file(self, path: str):
        with open(path, 'wb') as file:
            dump(self, file)
