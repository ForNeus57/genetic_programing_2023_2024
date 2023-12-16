from __future__ import annotations
from dataclasses import dataclass

from src.genetic.individual.structure.grammar_node import GrammarNode


@dataclass(slots=True, frozen=True)
class Expression(GrammarNode):
    @classmethod
    def from_random(cls) -> Expression:

        pass

    def mutate(self) -> Expression:
        pass

    def crossover(self, other: Expression) -> Expression:
        pass
