from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class Rule(ABC):

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


@dataclass(slots=True)
class RestrictedRandomize(ABC):
    meta: Any

    @classmethod
    @abstractmethod
    def from_random(cls, meta: Any) -> RestrictedRandomize:
        pass
