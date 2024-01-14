from abc import ABC, abstractmethod
from itertools import cycle
from typing import Literal, Union


class InputOutputOperation(ABC):

    @abstractmethod
    def read(self, hint: Literal['int', 'bool']) -> Union[int, bool]:
        pass

    @abstractmethod
    def write(self, value: Union[int, bool]) -> None:
        pass


class ConsoleInputOutputOperation(InputOutputOperation):

    def read(self, hint: Literal['int', 'bool']) -> Union[int, bool]:
        if hint == 'bool':
            return bool(input())
        else:
            return int(input())

    def write(self, value: Union[int, bool]) -> None:
        print(value)


class BufferInputOutputOperation(InputOutputOperation):
    def __init__(self, input_buffer: list[Union[int, bool]]):
        self.input_buffer: cycle[Union[int, bool]] = cycle(input_buffer)
        self.output: list[Union[int, bool]] = []

    def read(self, hint: Literal['int', 'bool']) -> Union[int, bool]:
        return next(self.input_buffer)

    def write(self, value: Union[int, bool]) -> None:
        self.output.append(value)
