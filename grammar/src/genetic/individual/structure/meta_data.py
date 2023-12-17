from dataclasses import dataclass

from src.genetic.individual.structure.tokens import VariableNameToken


@dataclass(frozen=True)
class MetaData:
    variables: set[VariableNameToken]

