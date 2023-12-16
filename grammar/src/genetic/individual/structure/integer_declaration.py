from __future__ import annotations
from dataclasses import dataclass
from typing import Optional
from random import choice

from src.genetic.individual.structure.expression import Expression
from src.genetic.individual.structure.grammar_node import GrammarNode
from src.genetic.individual.tokens.tokens import VariableNameToken


@dataclass(slots=True, frozen=True)
class IntegerDeclaration(GrammarNode):
    name: VariableNameToken
    expression: Optional[Expression]

    @classmethod
    def from_random(cls) -> IntegerDeclaration:
        name: VariableNameToken = VariableNameToken.from_random()
        expression: Optional[Expression] = choice([None, Expression.from_random()])

        return cls(name, expression)

    def mutate(self) -> IntegerDeclaration:
        pass

    def crossover(self, other: IntegerDeclaration) -> IntegerDeclaration:
        pass

    def __str__(self):
        base: str = f'int {self.name}'
        if self.expression is not None:
            return base + f' = {self.expression}'

        return base
