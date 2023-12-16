from __future__ import annotations
from dataclasses import dataclass
from typing import Optional

from src.genetic.individual.structure.execution_block import ExecutionBlock
from src.genetic.individual.structure.grammar_node import GrammarNode


@dataclass(slots=True, frozen=True)
class Program(GrammarNode):
    body: ExecutionBlock

    @classmethod
    def from_random(cls, max_size: int) -> Optional[Program]:
        if max_size <= 2:
            return None

        block: ExecutionBlock = ExecutionBlock.from_random(max_size - 1)
        return cls(block.size + 1, block)

    def mutate(self) -> Program:
        mutated_body: ExecutionBlock = self.body.mutate()
        return Program(mutated_body.size + 1, mutated_body)

    def crossover(self, other: Program) -> Program:
        if isinstance(other, Program):
            crossover_body: ExecutionBlock = self.body.crossover(other.body)
            return Program(crossover_body.size + 1, crossover_body)

        raise TypeError(f"Cannot crossover with {type(other)}.")

    def __str__(self) -> str:
        return str(self.body)
