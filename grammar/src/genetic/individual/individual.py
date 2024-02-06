from __future__ import annotations

import operator
from dataclasses import dataclass
from pickle import dump, load
from typing import Literal, Optional, TypeVar

from src.genetic.evaluation.evaluation import FitnessFunctionBase
from src.genetic.individual.structure.metadata import Metadata
from src.genetic.individual.structure.rules import Program
from src.genetic.interpreter.input_output import BufferInputOutputOperation
from src.genetic.interpreter.interpreter import Interpreter

T = TypeVar('T', float, int)


@dataclass(slots=True, frozen=True, order=False)
class Individual:
    program: Program

    @classmethod
    def from_file(cls, path: str) -> Individual:
        with open(path, 'rb') as file:
            return load(file)

    @classmethod
    def from_random(cls, meta: Optional[Metadata] = None) -> Individual:
        if meta is None:
            meta = Metadata()
        program: Program = Program.from_random(meta)
        return cls(program)

    def execute(self, input_vector: tuple) -> list:
        program_structure: str = str(self.program)
        output: Optional[BufferInputOutputOperation] = Interpreter.interpret(program_structure,
                                                                             BufferInputOutputOperation(
                                                                                 input_vector))
        if output is None:
            raise ValueError('Interpreter returned None!')

        return output.output

    def evaluate(self, fitness_function: FitnessFunctionBase, input_vector: tuple) -> T:
        result_vector: list = self.execute(input_vector)

        return fitness_function.calculate_fitness(tuple(result_vector), input_vector)

    def mutate(self) -> None:
        self.program.mutate()

    def crossover(self, other: Individual) -> None:
        self.program.crossover(other.program)

    def save_to_file(self, path: str) -> None:
        with open(path, 'wb') as file:
            dump(self, file)

    def __str__(self) -> str:
        return str(self.program)

    def __len__(self) -> int:
        return len(self.program)

    @staticmethod
    def tournament(individuals_join_fitness: list, mode: Literal['min', 'max']) -> tuple[int, int | float, Individual]:
        if mode == 'min':
            return min(individuals_join_fitness, key=operator.itemgetter(0))
        elif mode == 'max':
            return max(individuals_join_fitness, key=operator.itemgetter(0))

        raise ValueError(f'Unknown mode: {mode}')
