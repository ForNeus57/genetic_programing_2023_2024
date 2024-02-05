from __future__ import annotations

from dataclasses import dataclass
from random import choice, randint
from string import ascii_letters, digits
from typing import ClassVar

from src.genetic.individual.structure.node_types import Token
from src.genetic.individual.structure.limiters import RandomLimiter


@dataclass(slots=True, frozen=True)
class BooleanToken(Token):
    value: bool

    @classmethod
    def from_random(cls) -> BooleanToken:
        value: bool = choice([True, False])
        return cls(value)

    def __str__(self):
        return str(self.value).lower()


@dataclass(slots=True, frozen=True)
class IntegerToken(Token):
    value: int
    min_value: ClassVar[int] = -64
    max_value: ClassVar[int] = 64

    @classmethod
    def from_random(cls) -> IntegerToken:
        value: int = randint(cls.min_value, cls.max_value)
        return cls(value)

    def __str__(self):
        return str(self.value)


@dataclass(slots=True, frozen=True, order=True)
class VariableNameToken(Token):
    value: str

    forbidden_names: ClassVar[set[str]] = frozenset({
        'int',
        'bool',
        'read',
        'write',
        'if',
        'else',
        'while',
        'true',
        'false',
    })

    @classmethod
    def from_random(cls) -> VariableNameToken:
        name: str = cls._generate_random_name()
        return cls(name)

    @classmethod
    def _generate_random_name(cls) -> str:
        output = choice(ascii_letters)

        generator: RandomLimiter = RandomLimiter()
        full_character_set = ascii_letters + digits + '_'

        while generator.allow() or output in cls.forbidden_names:
            output += choice(full_character_set)

        return output

    def __str__(self):
        return str(self.value)


VariableTypes = BooleanToken | IntegerToken
