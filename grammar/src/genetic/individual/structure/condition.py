from __future__ import annotations
from dataclasses import dataclass
from typing import Union, Tuple, List
from random import choice

from src.genetic.individual.structure.expression import Expression
from src.genetic.individual.structure.grammar_node import GrammarNode
from src.genetic.individual.tokens.tokens import BooleanToken, VariableNameToken


@dataclass(slots=True, frozen=True)
class Condition(GrammarNode):
    body: ConditionType

    @classmethod
    def from_random(cls) -> Condition:
        table_of_choices: List[ConditionType] = [
            (Expression.from_random(), choice(['==', '!=', '>', '<', '>=', '<=']), Expression.from_random()),
            (Condition.from_random(), choice(['&&', '||', '^']), Condition.from_random(), Condition.from_random()),
            Condition.from_random(),
            VariableNameToken.from_random(),
            BooleanToken.from_random(),
        ]
        return cls(choice(table_of_choices))

    def mutate(self) -> Condition:
        pass

    def crossover(self, other: Condition) -> Condition:
        pass

    def __str__(self):
        match self.body:
            case (Expression(_) as left, operation, Expression(_) as right):
                return f'{left} {operation} {right}'

            case (Condition(_) as left, operation, Condition(_) as right):
                return f'{left} {operation} {right}'

            case Condition(_) as value:
                return f'!{str(value)}'

            case _ as value:
                return str(value)


ConditionType = Union[Tuple[Condition, str, Condition],
                      Tuple[Expression, str, Expression],
                      Condition,
                      VariableNameToken,
                      BooleanToken]
