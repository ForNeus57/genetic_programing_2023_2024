from __future__ import annotations
from dataclasses import dataclass
from abc import ABC, abstractmethod


@dataclass(slots=True, frozen=True)
class GrammarNode(ABC):

    @classmethod
    @abstractmethod
    def from_random(cls) -> GrammarNode:
        pass

    @abstractmethod
    def mutate(self) -> GrammarNode:
        pass

    @abstractmethod
    def crossover(self, other: GrammarNode) -> GrammarNode:
        pass






