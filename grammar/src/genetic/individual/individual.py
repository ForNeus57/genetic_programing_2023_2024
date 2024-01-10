from __future__ import annotations
from dataclasses import dataclass
from pickle import dump, load
from typing import Callable, Union, Literal

from src.genetic.individual.structure.rules import Program


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

    def execute(self, input_vector: tuple) -> tuple:
        raise NotImplementedError()

    def evaluate(self, fitness_function: Callable[[tuple, tuple],  Union[float, int, bool]],
                 input_vector: tuple,
                 model_vector: tuple) -> Union[float, int, bool]:
        result_vector: tuple = self.execute(input_vector)

        return fitness_function(result_vector, model_vector)

    def mutate(self) -> Individual:
        raise NotImplementedError()

    def crossover(self, other: Individual) -> Individual:
        raise NotImplementedError()

    def save_to_file(self, path: str):
        with open(path, 'wb') as file:
            dump(self, file)

    @staticmethod
    def tournament(individuals: tuple[Individual, ...],
                   fitness_function: Callable[[tuple, tuple],  Union[float, int, bool]],
                   input_vector: tuple,
                   model_vector: tuple,
                   mode: Literal['min', 'max']) -> Individual:
        if mode == 'min':
            return min(individuals, key=lambda individual: individual.evaluate(fitness_function, input_vector, model_vector))
        elif mode == 'max':
            return max(individuals, key=lambda individual: individual.evaluate(fitness_function, input_vector, model_vector))

        raise ValueError(f'Unknown mode: {mode}')
