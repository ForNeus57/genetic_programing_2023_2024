from __future__ import annotations
from dataclasses import dataclass
from abc import ABC, abstractmethod
from typing import ClassVar


@dataclass(slots=True, frozen=True)
class Rule(ABC):
    mutation_node_probability: ClassVar[float] = 0.2

    @abstractmethod
    def mutate(self) -> None:
        pass

    @abstractmethod
    def crossover(self, other: Rule) -> None:
        pass


@dataclass(slots=True, frozen=True)
class Token(ABC):
    raw: str
