from __future__ import annotations
from dataclasses import dataclass

from src.genetic.individual.structure.grammar_node import GrammarNode


@dataclass(slots=True, frozen=True)
class IntegerDeclaration(GrammarNode):
    @classmethod
    def from_random(cls) -> IntegerDeclaration:

        pass

    def mutate(self) -> IntegerDeclaration:
        pass

    def crossover(self, other: IntegerDeclaration) -> IntegerDeclaration:
        pass
