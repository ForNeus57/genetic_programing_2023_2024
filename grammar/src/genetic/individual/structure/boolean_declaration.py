from __future__ import annotations
from dataclasses import dataclass

from src.genetic.individual.structure.grammar_node import GrammarNode


@dataclass(slots=True, frozen=True)
class BooleanDeclaration(GrammarNode):
    @classmethod
    def from_random(cls) -> BooleanDeclaration:

        pass

    def mutate(self) -> BooleanDeclaration:
        pass

    def crossover(self, other: BooleanDeclaration) -> BooleanDeclaration:
        pass
