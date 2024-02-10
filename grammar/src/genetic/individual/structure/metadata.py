from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum, auto
from random import choice

from src.genetic.individual.structure.limiters import AdaptiveLimiter, Limiter


class GenerationMethod(Enum):
    GROW = 0
    FULL = auto()


@dataclass(slots=True)
class Metadata:
    variables_scope: set[str] = field(default_factory=set)
    depth: int = 0
    method: GenerationMethod = GenerationMethod.GROW
    limiter: Limiter = field(default_factory=AdaptiveLimiter)

    max_depth: int = 2

    @classmethod
    def from_dummy(cls) -> Metadata:
        return cls(
            set(),
            -1,
            GenerationMethod.GROW,
            AdaptiveLimiter(
                0.0,
                -1
            ),
            -1
        )

    def get_random_name(self) -> str:
        return choice(tuple(self.variables_scope))

    def is_depth_in_limits(self) -> bool:
        return self.depth < self.max_depth

    def is_empty(self):
        return len(self.variables_scope) == 0
