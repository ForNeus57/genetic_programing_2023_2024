from __future__ import annotations
from dataclasses import dataclass
from typing import Optional
from random import choice

from src.genetic.individual.structure.condition import Condition
from src.genetic.individual.structure.execution_block import ExecutionBlock
from src.genetic.individual.structure.grammar_node import GrammarNode


@dataclass(slots=True, frozen=True)
class IfStatement(GrammarNode):
    condition: Condition
    body: ExecutionBlock
    else_statement: Optional[ExecutionBlock]

    @classmethod
    def from_random(cls) -> IfStatement:
        condition: Condition = Condition.from_random()
        body: ExecutionBlock = ExecutionBlock.from_random()
        else_statement: ExecutionBlock = choice([None, ExecutionBlock.from_random()])

        return cls(condition, body, else_statement)

    def mutate(self) -> IfStatement:
        pass

    def crossover(self, other: IfStatement) -> IfStatement:
        pass

    def __str__(self):
        base: str = f'if ({self.condition}) {self.body}'

        if self.else_statement is not None:
            return base + f' else {self.else_statement}'

        return base
