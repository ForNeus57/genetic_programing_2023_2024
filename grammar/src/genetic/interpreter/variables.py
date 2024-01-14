from dataclasses import dataclass, field
from typing import Literal, Union


@dataclass(slots=True)
class Variable:
    is_constant: bool
    type: Literal['int', 'bool']
    value: Union[int, bool, None] = field(default=None)
