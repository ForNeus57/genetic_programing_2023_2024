from __future__ import annotations
from dataclasses import dataclass

from src.genetic.individual.structure.grammar_node import GrammarNode


@dataclass(slots=True, frozen=True)
class LoopStatement(GrammarNode):
    @classmethod
    def from_random(cls) -> LoopStatement:

        pass

    def mutate(self) -> LoopStatement:
        pass

    def crossover(self, other: LoopStatement) -> LoopStatement:
        pass
