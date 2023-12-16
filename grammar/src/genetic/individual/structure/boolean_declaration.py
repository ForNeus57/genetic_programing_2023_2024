from __future__ import annotations
from dataclasses import dataclass
from typing import Optional
from random import choice

from src.genetic.individual.structure.condition import Condition
from src.genetic.individual.structure.grammar_node import GrammarNode
from src.genetic.individual.tokens.tokens import VariableNameToken


@dataclass(slots=True, frozen=True)
class BooleanDeclaration(GrammarNode):
    name: VariableNameToken
    condition: Optional[Condition]

    @classmethod
    def from_random(cls) -> BooleanDeclaration:
        name: VariableNameToken = VariableNameToken.from_random()
        condition: Optional[Condition] = choice([None, Condition.from_random()])

        return cls(name, condition)

    def mutate(self) -> BooleanDeclaration:
        pass

    def crossover(self, other: BooleanDeclaration) -> BooleanDeclaration:
        pass

    def __str__(self):
        base: str = f'bool {self.name}'
        if self.condition is not None:
            return base + f' = {self.condition}'

        return base
