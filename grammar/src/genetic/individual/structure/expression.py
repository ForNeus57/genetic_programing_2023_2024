from __future__ import annotations
from dataclasses import dataclass
from typing import Union, Tuple, List
from random import choice

from src.genetic.individual.structure.grammar_node import GrammarNode
from src.genetic.individual.tokens.tokens import VariableNameToken, IntegerToken


@dataclass(slots=True, frozen=True)
class Expression(GrammarNode):
    body: ExpressionType

    @classmethod
    def from_random(cls) -> Expression:
        table_of_choices: List[ExpressionType] = [
            (Expression.from_random(), choice(['+', '-', '*', '/']), Expression.from_random()),
            VariableNameToken.from_random(),
            IntegerToken.from_random(),
        ]
        return cls(choice(table_of_choices))

    def mutate(self) -> Expression:
        pass

    def crossover(self, other: Expression) -> Expression:
        pass

    def __str__(self):
        match self.body:
            case (Expression(_) as left, operation, Expression(_) as right):
                return f'{left} {operation} {right}'

            case _ as value:
                return str(value)


ExpressionType = Union[Tuple[Expression, str, Expression],
                       VariableNameToken,
                       IntegerToken]
