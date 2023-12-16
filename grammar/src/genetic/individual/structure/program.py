from __future__ import annotations
from dataclasses import dataclass

from src.genetic.individual.structure.execution_block import ExecutionBlock
from src.genetic.individual.structure.grammar_node import GrammarNode


@dataclass(slots=True, frozen=True)
class Program(GrammarNode):
    body: ExecutionBlock

    @classmethod
    def from_random(cls) -> Program:
        block: ExecutionBlock = ExecutionBlock.from_random()
        return cls(block)

    def mutate(self) -> Program:
        pass

    def crossover(self, other: Program) -> Program:
        pass

    def __str__(self) -> str:
        return str(self.body)
