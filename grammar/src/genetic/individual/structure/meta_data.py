from dataclasses import dataclass

from genetic.individual.structure.tokens import VariableNameToken


@dataclass(frozen=True)
class MetaData:
    variables: set[VariableNameToken]

