from __future__ import annotations
from dataclasses import dataclass
from random import choice
from typing import Union

from src.genetic.individual.structure.boolean_declaration import BooleanDeclaration
from src.genetic.individual.structure.grammar_node import GrammarNode
from src.genetic.individual.structure.integer_declaration import IntegerDeclaration

DeclarationTypes = Union[IntegerDeclaration, BooleanDeclaration]


@dataclass(slots=True, frozen=True)
class VarDeclaration(GrammarNode):
    is_constant: bool
    declaration: DeclarationTypes

    @classmethod
    def from_random(cls) -> VarDeclaration:
        is_constant = choice([True, False])
        declaration: DeclarationTypes = choice([IntegerDeclaration, BooleanDeclaration]).from_random()

        return cls(is_constant, declaration)

    def mutate(self) -> VarDeclaration:
        pass

    def crossover(self, other: VarDeclaration) -> VarDeclaration:
        pass

    def __str__(self):
        return f'{"const " if self.is_constant else ""}{self.declaration};'
