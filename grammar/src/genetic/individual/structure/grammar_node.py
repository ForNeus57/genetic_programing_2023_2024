from __future__ import annotations
from dataclasses import dataclass
from abc import ABC, abstractmethod
from typing import Optional


@dataclass(slots=True, frozen=True)
class GrammarNode(ABC):
    size: int

    @classmethod
    @abstractmethod
    def from_random(cls, max_size: int) -> Optional[GrammarNode]:
        pass

    @abstractmethod
    def mutate(self) -> GrammarNode:
        pass

    @abstractmethod
    def crossover(self, other: GrammarNode) -> GrammarNode:
        pass




