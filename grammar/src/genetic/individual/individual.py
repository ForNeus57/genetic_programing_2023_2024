from __future__ import annotations
from dataclasses import dataclass
from pickle import dump, load
from typing import Callable, Union, Literal, Optional

from src.genetic.individual.structure.tokens import Metadata
from src.genetic.individual.structure.rules import Program
from src.genetic.interpreter.input_output import BufferInputOutputOperation
from src.genetic.interpreter.interpreter import Interpreter


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

    def __str__(self) -> str:
        return str(self.program)

    def execute(self, input_vector: tuple) -> tuple:
        program_structure: str = str(self.program)
        output: Optional[BufferInputOutputOperation] = Interpreter.interpret(program_structure,
                                                                             BufferInputOutputOperation(
                                                                                 list(input_vector)))
        if output is None:
            raise ValueError('Interpreter returned None!')

        return tuple(output.output)

    def evaluate(self, fitness_function: Callable[[tuple, tuple], Union[float, int, bool]],
                 input_vector: tuple,
                 model_vector: tuple) -> Union[float, int, bool]:
        result_vector: tuple = self.execute(input_vector)

        return fitness_function(result_vector, model_vector)

    def mutate(self) -> None:
        self.program.mutate()

    def crossover(self, other: Individual) -> None:
        self.program.crossover(other.program)

    def save_to_file(self, path: str):
        with open(path, 'wb') as file:
            dump(self, file)

    @staticmethod
    def tournament(individuals: tuple[Individual, ...],
                   fitness_function: Callable[[tuple, tuple], Union[float, int, bool]],
                   input_vector: tuple,
                   model_vector: tuple,
                   mode: Literal['min', 'max']) -> Individual:
        if mode == 'min':
            return min(individuals,
                       key=lambda individual: individual.evaluate(fitness_function, input_vector, model_vector))
        elif mode == 'max':
            return max(individuals,
                       key=lambda individual: individual.evaluate(fitness_function, input_vector, model_vector))

        raise ValueError(f'Unknown mode: {mode}')
