from __future__ import annotations
from dataclasses import dataclass
from typing import ClassVar

from src.genetic.individual.structure.execution_block import ExecutionBlock
from src.genetic.individual.structure.grammar_node import GrammarNode


@dataclass(slots=True, frozen=True)
class Program(GrammarNode):
    body: ExecutionBlock
    self_size: ClassVar[int] = 1

    @classmethod
    def from_random(cls, max_size: int) -> Program:
        if max_size < cls.minimum_size():
            raise ValueError("Unable to construct program, because maximum size constraints are too harsh.")

        block: ExecutionBlock = ExecutionBlock.from_random(max_size - cls.self_size)
        return cls(block.size + cls.self_size, block)

    @classmethod
    def minimum_size(cls) -> int:
        return ExecutionBlock.minimum_size() + cls.self_size

    def mutate(self) -> Program:
        pass

    def crossover(self, other: Program) -> Program:
        pass

    def __str__(self) -> str:
        return str(self.body)
