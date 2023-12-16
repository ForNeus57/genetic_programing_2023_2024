from __future__ import annotations
from dataclasses import dataclass

from src.genetic.individual.structure.grammar_node import GrammarNode


@dataclass(slots=True, frozen=True)
class Statement(GrammarNode):
    @classmethod
    def from_random(cls) -> Statement:
        
        pass

    def mutate(self) -> Statement:
        pass

    def crossover(self, other: Statement) -> Statement:
        pass
