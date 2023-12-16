from __future__ import annotations
from dataclasses import dataclass

from src.genetic.individual.structure.condition import Condition
from src.genetic.individual.structure.execution_block import ExecutionBlock
from src.genetic.individual.structure.grammar_node import GrammarNode


@dataclass(slots=True, frozen=True)
class LoopStatement(GrammarNode):
    condition: Condition
    body: ExecutionBlock

    @classmethod
    def from_random(cls) -> LoopStatement:
        condition: Condition = Condition.from_random()
        body: ExecutionBlock = ExecutionBlock.from_random()

        return cls(condition, body)

    def mutate(self) -> LoopStatement:
        pass

    def crossover(self, other: LoopStatement) -> LoopStatement:
        pass

    def __str__(self):
        return f'while ({self.condition}) {self.body}'
