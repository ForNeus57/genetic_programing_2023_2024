from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any


class Crossover(ABC):
    @abstractmethod
    def crossover(self, other: Crossover) -> None:
        pass


class Mutable(ABC):
    @abstractmethod
    def mutate(self) -> None:
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
