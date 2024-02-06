from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum, auto
from random import choice

from src.genetic.individual.structure.limiters import AdaptiveLimiter


class GenerationMethod(Enum):
    GROW = 0
    FULL = auto()


@dataclass()
class Metadata:
    variables_scope: set[str] = field(default_factory=set)
    depth: int = 0
    method: GenerationMethod = GenerationMethod.GROW
    limiter = AdaptiveLimiter()

    max_depth: int = 2

    def get_random_name(self) -> str:
        return choice(tuple(self.variables_scope))

    def is_depth_in_limits(self) -> bool:
        return self.depth < Metadata.max_depth

    def is_empty(self):
        return len(self.variables_scope) == 0
