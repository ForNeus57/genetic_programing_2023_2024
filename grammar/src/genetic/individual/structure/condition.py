from __future__ import annotations
from dataclasses import dataclass

from src.genetic.individual.structure.grammar_node import GrammarNode


@dataclass(slots=True, frozen=True)
class Condition(GrammarNode):
    @classmethod
    def from_random(cls) -> Condition:

        pass

    def mutate(self) -> Condition:
        pass

    def crossover(self, other: Condition) -> Condition:
        pass
