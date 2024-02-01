from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum, auto
from random import choice
from typing import ClassVar, Optional, Literal

from src.genetic.individual.structure.limiters import HardLimiter
from src.genetic.interpreter.variables import Variable


class GenerationMethod(Enum):
    GROW = 0
    FULL = auto()


@dataclass()
class Metadata:
    variables_scope: dict[str, Variable] = field(default_factory=dict)
    depth: int = 0
    limiter = HardLimiter
    method: GenerationMethod = GenerationMethod.FULL

    mutation_node_probability: ClassVar[float] = 0.5
    mutation_from_start_probability: ClassVar[float] = 0.1
    crossover_node_probability: ClassVar[float] = 0.5

    max_depth: ClassVar[int] = 1

    def get_random_name(self, type_hint: Optional[Literal['int', 'bool']] = None) -> str:
        if type_hint is None:
            return choice([name for name, variable in self.variables_scope.items()])

        return choice([name for name, variable in self.variables_scope.items() if variable.type == type_hint])

    def has_boolean_variables(self) -> bool:
        return any(map(lambda x: x.type == 'bool', self.variables_scope.values()))

    def has_integer_variables(self) -> bool:
        return any(map(lambda x: x.type == 'int', self.variables_scope.values()))

    def get_variable(self, name: str) -> Variable:
        return self.variables_scope[name]

    def is_depth_in_limits(self) -> bool:
        return self.depth < Metadata.max_depth

    def is_empty(self):
        return len(self.variables_scope) == 0
