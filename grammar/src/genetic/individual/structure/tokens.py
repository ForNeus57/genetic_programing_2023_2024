from __future__ import annotations

from dataclasses import dataclass
from random import choice, randint, random
from typing import ClassVar
from string import ascii_letters, digits

from genetic.individual.probability.exponential_probability import ExponentialProbability
from genetic.individual.interfaces.node_types import Token
from genetic.individual.interfaces.randomize import Randomize


@dataclass(slots=True, frozen=True)
class BooleanToken(Token, Randomize):
    value: bool

    @classmethod
    def from_random(cls) -> BooleanToken:
        value: bool = choice([True, False])
        return cls(str(value), value)

    def __str__(self):
        return str(self.value)


@dataclass(slots=True, frozen=True)
class IntegerToken(Token, Randomize):
    value: int
    min_value: ClassVar[int] = -255
    max_value: ClassVar[int] = 255

    @classmethod
    def from_random(cls) -> IntegerToken:
        value: int = randint(cls.min_value, cls.max_value)
        return cls(str(value), value)

    def __str__(self):
        return str(self.value)


@dataclass(slots=True, frozen=True, order=True)
class VariableNameToken(Token, Randomize):
    value: str

    @classmethod
    def from_random(cls) -> VariableNameToken:
        name: str = cls._generate_random_name()
        return cls(f'\"{name}\"', name)

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
