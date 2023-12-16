from __future__ import annotations
from dataclasses import dataclass
from enum import Enum, auto
from random import choice

from src.genetic.individual.structure.grammar_node import GrammarNode
from src.genetic.individual.tokens.tokens import VariableNameToken


class IOType(Enum):
    READ = 0,
    WRITE = auto()

    def __str__(self):
        return self.name.lower()

    @classmethod
    def from_random(cls) -> IOType:
        return choice(list(cls))


@dataclass(slots=True, frozen=True)
class IOStatement(GrammarNode):
    io_type: IOType
    name: VariableNameToken

    @classmethod
    def from_random(cls) -> IOStatement:
        io_type: IOType = IOType.from_random()
        name: VariableNameToken = VariableNameToken.from_random()
        return cls(io_type, name)

    def mutate(self) -> IOStatement:
        pass

    def crossover(self, other: IOStatement) -> IOStatement:
        pass

    def __str__(self):
        return f'{self.io_type} ({self.name});'
