from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any

from src.genetic.interpreter.context import InterpreterContext


class Crossover(ABC):
    @abstractmethod
    def crossover(self, other: Crossover) -> None:
        pass


class Rule(ABC):
    @abstractmethod
    def mutate(self) -> None:
        pass

    @abstractmethod
    def visit_commands(self, context: InterpreterContext) -> Any:
        pass

    def visit(self, context: InterpreterContext) -> Any:
        context.enter_instruction()
        return self.visit_commands(context)


class Token(ABC):

    @classmethod
    @abstractmethod
    def from_random(cls) -> Token:
        pass


@dataclass(slots=True)
class RestrictedRandomize(ABC):
    meta: Any

    @classmethod
    @abstractmethod
    def from_random(cls, meta: Any) -> RestrictedRandomize:
        pass
