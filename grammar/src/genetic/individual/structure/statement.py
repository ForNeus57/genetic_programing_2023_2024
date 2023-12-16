from typing import Optional

from src.genetic.individual.structure.grammar_node import GrammarNode


class Statement(GrammarNode):
    @classmethod
    def from_random(cls, max_size: int) -> Optional[GrammarNode]:
        pass

    @classmethod
    def minimum_size(cls) -> int:
        pass

    def mutate(self) -> GrammarNode:
        pass

    def crossover(self, other: GrammarNode) -> GrammarNode:
        pass