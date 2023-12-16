from __future__ import annotations
from dataclasses import dataclass

from src.genetic.individual.structure.grammar_node import GrammarNode


@dataclass(slots=True, frozen=True)
class Assigment(GrammarNode):
    @classmethod
    def from_random(cls) -> Assigment:

        pass

    def mutate(self) -> Assigment:
        pass

    def crossover(self, other: Assigment) -> Assigment:
        pass
