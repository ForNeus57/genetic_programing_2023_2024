from __future__ import annotations
from dataclasses import dataclass, field

from src.genetic.individual.meta_data import MetaData
from src.genetic.individual.structure.grammar_node import GrammarNode
from src.genetic.individual.structure.statement import Statement


@dataclass(slots=True, frozen=True)
class ExecutionBlock(GrammarNode):
    meta_data: MetaData
    statements: list[Statement] = field(default_factory=list)

    @classmethod
    def from_random(cls, max_size: int) -> ExecutionBlock:
        body: list[Statement] = []



        return cls(sum([child.size for child in body]) + 1, None, body)

    def mutate(self) -> ExecutionBlock:
        pass

    def crossover(self, other: ExecutionBlock) -> ExecutionBlock:
        pass

    def __str__(self) -> str:
        statements_print = ''.join([str(statement) for statement in self.statements])
        return f'{{\n{statements_print}}}\n'
