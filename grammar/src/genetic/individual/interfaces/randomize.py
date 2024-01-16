from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from enum import Enum, auto
from random import choice, randint, random
from string import ascii_letters, digits
from typing import ClassVar, Callable

from src.genetic.individual.interfaces.node_types import Token
from src.genetic.individual.limiters.exponential_probability import ExponentialProbability

from src.genetic.individual.limiters.limiters import HardLimiter, AdaptiveLimiter, RandomLimiter



@dataclass(slots=True, frozen=True)
class RestrictedRandomize(ABC):
    meta: Metadata

    @classmethod
    @abstractmethod
    def from_random(cls, meta: Metadata) -> RestrictedRandomize:
        pass


@dataclass(slots=True, frozen=True)
class BooleanToken(Token):
    value: bool

    @classmethod
    def from_random(cls) -> BooleanToken:
        value: bool = choice([True, False])
        return cls(value)

    def __str__(self):
        return str(self.value)


@dataclass(slots=True, frozen=True)
class IntegerToken(Token):
    value: int
    min_value: ClassVar[int] = -255
    max_value: ClassVar[int] = 255

    @classmethod
    def from_random(cls) -> IntegerToken:
        value: int = randint(cls.min_value, cls.max_value)
        return cls(value)

    def __str__(self):
        return str(self.value)


@dataclass(slots=True, frozen=True, order=True)
class VariableNameToken(Token):
    value: str

    @classmethod
    def from_random(cls) -> VariableNameToken:
        name: str = cls._generate_random_name()
        return cls(name)

    @classmethod
    def _generate_random_name(cls) -> str:
        output = choice(ascii_letters)

        probability_generator: ExponentialProbability = ExponentialProbability()
        full_character_set = ascii_letters + digits + '_'

        while next(probability_generator) > random():
            output += choice(full_character_set)

        return output

    def __str__(self):
        return str(self.value)


VariableTypes = BooleanToken | IntegerToken

class RandomGenerationMethod(Enum):
    GROW = 0
    FULL = auto()
    RAMPED_HALF_AND_HALF = auto()


@dataclass()
class Metadata:
    variables_scope: set[VariableNameToken] = field(default_factory=set)
    depth: int = 0
    limiter = HardLimiter
    method: RandomGenerationMethod = RandomGenerationMethod.GROW

    max_depth: ClassVar[int] = 5

    def get_random_name(self) -> VariableNameToken:
        return choice(tuple(self.variables_scope))

    def is_depth_in_limits(self) -> bool:
        return self.depth < Metadata.max_depth

    def is_empty(self):
        return len(self.variables_scope) == 0
