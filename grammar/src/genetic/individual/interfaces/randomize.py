from __future__ import annotations
from abc import ABC, abstractmethod


class Randomize(ABC):

    @classmethod
    @abstractmethod
    def from_random(cls) -> Randomize:
        pass


class RestrictedRandomize(ABC):

    @classmethod
    @abstractmethod
    def from_random(cls, depth: int) -> RestrictedRandomize:
        pass
