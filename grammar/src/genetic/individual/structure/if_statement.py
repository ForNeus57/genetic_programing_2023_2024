from __future__ import annotations
from dataclasses import dataclass

from src.genetic.individual.structure.grammar_node import GrammarNode


@dataclass(slots=True, frozen=True)
class IfStatement(GrammarNode):
    @classmethod
    def from_random(cls) -> IfStatement:

        pass

    def mutate(self) -> IfStatement:
        pass

    def crossover(self, other: IfStatement) -> IfStatement:
        pass
