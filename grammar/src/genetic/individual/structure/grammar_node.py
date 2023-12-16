from __future__ import annotations
from dataclasses import dataclass
from abc import ABC, abstractmethod
from typing import ClassVar


@dataclass(slots=True, frozen=True)
class GrammarNode(ABC):
    mutation_node_probability: ClassVar[float] = 0.2
    depth: int
    max_depth: ClassVar[int] = 5

    @classmethod
    @abstractmethod
    def from_random(cls, depth: int) -> GrammarNode:
        pass

    @abstractmethod
    def mutate(self) -> GrammarNode:
        pass

    @abstractmethod
    def crossover(self, other: GrammarNode) -> GrammarNode:
        pass






