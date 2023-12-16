from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class MetaData:
    variables: dict[str, Any]

