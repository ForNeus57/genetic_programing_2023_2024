from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum, auto
from random import choice
from typing import Optional, Literal

from src.genetic.individual.structure.limiters import HardLimiter


class GenerationMethod(Enum):
    GROW = 0
    FULL = auto()


@dataclass()
class Metadata:
    variables_scope: dict[str, Literal['int', 'bool']] = field(default_factory=dict)
    depth: int = 0
    limiter = HardLimiter()
    method: GenerationMethod = GenerationMethod.GROW

    mutation_node_probability: float = 0.5
    mutation_from_start_probability: float = 0.1
    crossover_node_probability: float = 0.5

    max_depth: int = 1

    def get_random_name(self, type_hint: Optional[Literal['int', 'bool']] = None) -> str:
        if type_hint is None:
            return choice([name for name, _ in self.variables_scope.items()])

        return choice([name for name, type_value in self.variables_scope.items() if type_value == type_hint])

    def has_boolean_variables(self) -> bool:
        return any(map(lambda x: x == 'bool', self.variables_scope.values()))

    def has_integer_variables(self) -> bool:
        return any(map(lambda x: x == 'int', self.variables_scope.values()))

    def get_variable(self, name: str) -> Literal['int', 'bool']:
        return self.variables_scope[name]

    def is_depth_in_limits(self) -> bool:
        return self.depth < Metadata.max_depth

    def is_empty(self):
        return len(self.variables_scope) == 0
