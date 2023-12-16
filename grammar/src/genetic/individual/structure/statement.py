from __future__ import annotations
from dataclasses import dataclass
from random import choice
from typing import Union

from pycparser.c_ast import Assignment

from src.genetic.individual.structure.grammar_node import GrammarNode
from src.genetic.individual.structure.if_statement import IfStatement
from src.genetic.individual.structure.io_statement import IOStatement
from src.genetic.individual.structure.loop_statement import LoopStatement
from src.genetic.individual.structure.var_declaration import VarDeclaration

BodyTypes = Union[VarDeclaration, Assignment, IfStatement, LoopStatement, IOStatement]


@dataclass(slots=True, frozen=True)
class Statement(GrammarNode):
    body: BodyTypes

    @classmethod
    def from_random(cls) -> Statement:
        statement_constructor = choice([VarDeclaration, Assignment, IfStatement, LoopStatement, IOStatement])
        body: BodyTypes = statement_constructor.from_random()
        return cls(body)

    def mutate(self) -> Statement:
        pass

    def crossover(self, other: Statement) -> Statement:
        pass

    def __str__(self):
        return str(self.body)
