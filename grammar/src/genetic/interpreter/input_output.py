from abc import ABC, abstractmethod
from itertools import cycle
from typing import Optional


class InputOutputOperation(ABC):

    @abstractmethod
    def read(self) -> int:
        pass

    @abstractmethod
    def write(self, value: int) -> None:
        pass


class ConsoleInputOutputOperation(InputOutputOperation):

    def read(self) -> int:
        return int(input())

    def write(self, value: int) -> None:
        print(value)


class BufferInputOutputOperation(InputOutputOperation):
    def __init__(self, input_buffer: Optional[tuple[int, ...]] = None):
        if input_buffer is None:
            input_buffer = (1, )

        self.input_ints: cycle[int] = cycle(input_buffer)

        self.output: list[int] = []

    def read(self) -> int:
        return next(self.input_ints)

    def write(self, value: int) -> None:
        self.output.append(value)
