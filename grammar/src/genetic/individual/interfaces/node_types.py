from __future__ import annotations
from dataclasses import dataclass
from abc import ABC, abstractmethod
from typing import ClassVar


@dataclass(slots=True)
class Rule(ABC):
    mutation_node_probability: ClassVar[float] = 0.5
    mutation_from_start_probability: ClassVar[float] = 0.1
    crossover_node_probability: ClassVar[float] = 0.5

    @abstractmethod
    def mutate(self) -> None:
        pass

    @abstractmethod
    def crossover(self, other: Rule) -> None:
        pass


class Token(ABC):

    @classmethod
    @abstractmethod
    def from_random(cls) -> Token:
        pass
