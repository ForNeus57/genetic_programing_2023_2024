from dataclasses import dataclass

from src.genetic.individual.tokens.tokens import VariableNameToken


@dataclass(frozen=True)
class MetaData:
    variables: set[VariableNameToken]

