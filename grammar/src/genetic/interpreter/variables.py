from dataclasses import dataclass
from typing import Literal, Union


@dataclass(slots=True)
class Variable:
    type: Literal['int', 'bool']
    value: Union[int, bool]
