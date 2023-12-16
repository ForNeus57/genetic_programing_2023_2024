from __future__ import annotations
from dataclasses import dataclass

from src.genetic.individual.structure.grammar_node import GrammarNode


@dataclass(slots=True, frozen=True)
class VarDeclaration(GrammarNode):
    @classmethod
    def from_random(cls) -> VarDeclaration:

        pass

    def mutate(self) -> VarDeclaration:
        pass

    def crossover(self, other: VarDeclaration) -> VarDeclaration:
        pass
