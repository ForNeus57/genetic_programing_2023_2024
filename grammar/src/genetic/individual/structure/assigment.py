from __future__ import annotations
from dataclasses import dataclass
from typing import Union
from random import choice

from src.genetic.individual.structure.condition import Condition
from src.genetic.individual.structure.expression import Expression
from src.genetic.individual.structure.grammar_node import GrammarNode
from src.genetic.individual.tokens.tokens import VariableNameToken

AssigmentValueType = Union[Expression, Condition]


@dataclass(slots=True, frozen=True)
class Assigment(GrammarNode):
    name: VariableNameToken
    assigment_value: AssigmentValueType

    @classmethod
    def from_random(cls) -> Assigment:
        name: VariableNameToken = VariableNameToken.from_random()
        value: AssigmentValueType = choice([Expression, Condition]).from_random()  # Don't forget Validation...

        return cls(name, value)

    def mutate(self) -> Assigment:
        pass

    def crossover(self, other: Assigment) -> Assigment:
        pass

    def __str__(self):
        return f'{self.name} = {self.assigment_value}'
