from abc import ABC, abstractmethod
from itertools import cycle
from typing import Literal, Union, Optional


class InputOutputOperation(ABC):

    @abstractmethod
    def read(self, hint: type) -> Union[int, bool]:
        pass

    @abstractmethod
    def write(self, value: Union[int, bool]) -> None:
        pass


class ConsoleInputOutputOperation(InputOutputOperation):

    def read(self, hint: type) -> Union[int, bool]:
        if hint is bool:
            return bool(input())
        else:
            return int(input())

    def write(self, value: Union[int, bool]) -> None:
        print(value)


class BufferInputOutputOperation(InputOutputOperation):
    def __init__(self, input_buffer: Optional[tuple[Union[int, bool]]] = None):
        if input_buffer is None:
            input_buffer = []

        only_bools: list[bool] = [*filter(lambda x: type(x) is bool, input_buffer)]
        only_ints: list[int] = [*filter(lambda x: type(x) is int, input_buffer)]

        if len(only_bools) == 0:
            only_bools.append(True)

        if len(only_ints) == 0:
            only_ints.append(1)

        self.input_bools: cycle[bool] = cycle(only_bools)
        self.input_ints: cycle[int] = cycle(only_ints)

        self.output: list[Union[int, bool]] = []

    def read(self, hint: type) -> Union[int, bool]:
        if hint is bool:
            return next(self.input_bools)

        return next(self.input_ints)

    def write(self, value: Union[int, bool]) -> None:
        self.output.append(value)
