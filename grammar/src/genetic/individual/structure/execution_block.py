from __future__ import annotations
from dataclasses import dataclass, field
from random import random

from src.genetic.individual.probability.subsequent_node_probability_generator import SubsequentNodeProbabilityGenerator
from src.genetic.individual.structure.grammar_node import GrammarNode
from src.genetic.individual.structure.statement import Statement


@dataclass(slots=True, frozen=True)
class ExecutionBlock(GrammarNode):
    statements: list[Statement] = field(default_factory=list)

    @classmethod
    def from_random(cls) -> ExecutionBlock:
        body: list[Statement] = []
        probability: SubsequentNodeProbabilityGenerator = SubsequentNodeProbabilityGenerator()

        while next(probability) > random():
            body.append(Statement.from_random())

        return cls(body)

    def mutate(self) -> ExecutionBlock:
        pass

    def crossover(self, other: ExecutionBlock) -> ExecutionBlock:
        pass

    def __str__(self) -> str:
        statements_print = ''.join([str(statement) for statement in self.statements])
        return f'{{\n{statements_print}}}\n'
