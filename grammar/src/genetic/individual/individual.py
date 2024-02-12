from __future__ import annotations

from dataclasses import dataclass, InitVar, field
from pathlib import Path
from pickle import dump, load
from typing import Literal, Optional

from src.genetic.evaluation.evaluation import FitnessFunctionBase
from src.genetic.individual.structure.metadata import Metadata
from src.genetic.individual.structure.rules import Program
from src.genetic.interpreter.context import InterpreterContext
from src.genetic.interpreter.input_output import BufferInputOutputOperation
from src.utilities.timeout import timeout


@dataclass(slots=True, frozen=True, order=False)
class Individual:
    program: Program

    # fitness: int | float = field(init=False)

    @classmethod
    def from_file(cls, path: Path) -> Individual:
        with open(path, 'rb') as file:
            return load(file)

    @classmethod
    def from_random(cls, meta: Optional[Metadata] = None) -> Individual:
        if meta is None:
            meta = Metadata()
        program: Program = Program.from_random(meta)
        return cls(program)

    # def __post_init__(self) -> None:
    #     self.fitness

    def execute(self, input_vector: Optional[tuple]) -> list:
        output: BufferInputOutputOperation = BufferInputOutputOperation(input_vector)

        try:
            self.program.visit(InterpreterContext(
                output
            ))
        except StopIteration:
            pass

        return output.output

    @timeout(4, 9_999_999)
    def evaluate(self, params: tuple[FitnessFunctionBase, Optional[tuple]]) -> int | float:
        fitness_function, input_vector = params
        result_vector: list = self.execute(input_vector)

        return fitness_function.calculate_fitness(tuple(result_vector), input_vector)

    def mutate(self) -> None:
        self.program.mutate()

    def crossover(self, other: Individual) -> None:
        self.program.crossover(other.program)

    def save_to_file(self, path: Path) -> None:
        with open(path, 'wb') as file:
            dump(self, file)

    def __str__(self) -> str:
        return str(self.program)

    def __len__(self) -> int:
        return len(self.program)

    @staticmethod
    def tournament(individuals_join_fitness: list, mode: Literal['min', 'max']) \
            -> tuple[int, tuple[int | float, Individual]]:
        if mode == 'min':
            return min(individuals_join_fitness, key=lambda x: x[1][0])
        elif mode == 'max':
            return max(individuals_join_fitness, key=lambda x: x[1][0])

        raise ValueError(f'Unknown mode: {mode}')
