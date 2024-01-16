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
        only_bools = [x for x in input_buffer if type(x) is bool]
        only_ints = [x for x in input_buffer if type(x) is int]

        if len(only_bools) == 0:
            only_bools.append(True)

        if len(only_ints) == 0:
            only_ints.append(1)

        self.input_bools: cycle[bool] = cycle(only_bools)
        self.input_ints: cycle[int] = cycle(only_ints)

        self.output: list[Union[int, bool]] = []

    def read(self, hint: Literal['int', 'bool']) -> Union[int, bool]:
        if hint == 'bool':
            return next(self.input_bools)
        else:
            return next(self.input_ints)

    def write(self, value: Union[int, bool]) -> None:
        self.output.append(value)
