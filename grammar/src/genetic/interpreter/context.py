from __future__ import annotations

from dataclasses import dataclass, field
from typing import Final, Optional

from src.genetic.interpreter.input_output import InputOutputOperation


@dataclass(slots=True)
class InterpreterContext:
    mode: InputOutputOperation
    instructions_limit: Final[int] = 200

    variables: dict[str, int] = field(default_factory=dict, init=False)
    used_instructions: int = field(default=0, init=False)

    def __getitem__(self, item: str) -> Optional[int]:
        return self.variables.get(item)

    def __setitem__(self, key: str, value: int) -> None:
        self.variables[key] = value

    def enter_instruction(self) -> None:
        if self.used_instructions >= self.instructions_limit:
            raise StopIteration(f'Interpreter exceeded instruction limit({self.instructions_limit})!')

        self.used_instructions += 1
