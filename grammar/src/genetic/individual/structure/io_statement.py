from __future__ import annotations
from dataclasses import dataclass

from src.genetic.individual.structure.grammar_node import GrammarNode


@dataclass(slots=True, frozen=True)
class IOStatement(GrammarNode):
    @classmethod
    def from_random(cls) -> IOStatement:

        pass

    def mutate(self) -> IOStatement:
        pass

    def crossover(self, other: IOStatement) -> IOStatement:
        pass
