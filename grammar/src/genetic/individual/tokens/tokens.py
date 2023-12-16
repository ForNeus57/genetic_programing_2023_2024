from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from random import choice, randint, random
from typing import ClassVar
from string import ascii_letters, digits

from src.genetic.individual.probability.subsequent_node_probability_generator import SubsequentNodeProbabilityGenerator


@dataclass(slots=True, frozen=True)
class Token(ABC):
    raw: str

    @classmethod
    @abstractmethod
    def from_random(cls) -> Token:
        pass


@dataclass(slots=True, frozen=True)
class BooleanToken(Token):
    value: bool

    @classmethod
    def from_random(cls) -> BooleanToken:
        value: bool = choice([True, False])
        return cls(str(value), value)


@dataclass(slots=True, frozen=True)
class IntegerToken(Token):
    value: int
    min_value: ClassVar[int] = -255
    max_value: ClassVar[int] = 255

    @classmethod
    def from_random(cls) -> IntegerToken:
        value: int = randint(IntegerToken.min_value, IntegerToken.max_value)
        return cls(str(value), value)


@dataclass(slots=True, frozen=True)
class VariableNameToken(Token):
    value: str

    @classmethod
    def from_random(cls) -> VariableNameToken:
        name: str = cls.generate_random_name()
        return cls(f'\"{name}\"', name)

    @classmethod
    def generate_random_name(cls) -> str:
        output = choice(ascii_letters)

        probability_generator: SubsequentNodeProbabilityGenerator = SubsequentNodeProbabilityGenerator(0.9, 0.8)
        full_character_set = ascii_letters + digits + '_'

        while next(probability_generator) > random():
            output += choice(full_character_set)

        return output

