from __future__ import annotations

import importlib
import inspect
from copy import deepcopy
from dataclasses import dataclass, field
from enum import Enum, auto
from random import choice, randint
from types import SimpleNamespace
from typing import Union, Optional, Tuple

from src.genetic.individual.structure.node_types import Crossover, RestrictedRandomize, Mutable
from src.genetic.individual.structure.limiters import Limiter
from src.genetic.individual.structure.metadata import Metadata, GenerationMethod
from src.genetic.individual.structure.tokens import VariableNameToken, IntegerToken, BooleanToken


@dataclass(slots=True)
class Program(Crossover, Mutable, RestrictedRandomize):
    body: ExecutionBlock

    @classmethod
    def from_random(cls, meta: Metadata) -> Program:
        block: ExecutionBlock = ExecutionBlock.from_random(meta)
        return cls(meta, block)

    def mutate(self) -> None:
        self.body.mutate()

    def crossover(self, other: Program) -> None:
        self.body.crossover(other.body)

    def __str__(self) -> str:
        return str(self.body)

    def __len__(self) -> int:
        return len(self.body)


@dataclass(slots=True)
class ExecutionBlock(Crossover, Mutable, RestrictedRandomize):
    statements: list[StatementBodyTypes] = field(default_factory=list)

    @classmethod
    def from_random(cls, meta: Metadata) -> ExecutionBlock:
        limiter: Limiter = deepcopy(meta.limiter)
        body: list[StatementBodyTypes] = []

        statement: StatementBodyTypes = cls.generate_random_body_element(meta)
        child_meta: Metadata = statement.meta
        body.append(statement)

        while limiter.allow():
            statement: StatementBodyTypes = cls.generate_random_body_element(child_meta)
            child_meta: Metadata = statement.meta
            body.append(statement)

        return cls(meta, body)

    @classmethod
    def generate_random_body_element(cls, meta: Metadata) -> StatementBodyTypes:
        table_of_choices: list = cls.generate_choices(meta)

        return choice(table_of_choices).from_random(meta)

    @classmethod
    def generate_choices(cls, meta: Metadata) -> list:
        match meta.method:
            case GenerationMethod.FULL:
                if meta.is_depth_in_limits():
                    return [
                        IfStatement,
                        LoopStatement,
                    ]

                output: list = [
                    IntegerDeclaration,
                    BooleanDeclaration,
                    IOStatement,
                ]
                if not meta.is_empty():
                    output.extend([
                        Assigment,
                    ])

                return output

            case GenerationMethod.GROW:
                output: list = [
                    IntegerDeclaration,
                    BooleanDeclaration,
                    IOStatement,
                ]
                if not meta.is_empty():
                    output.extend([
                        Assigment,
                    ])

                if meta.is_depth_in_limits():
                    output.extend([
                        IfStatement,
                        LoopStatement,
                    ])

                return output

    def mutate(self) -> None:
        choice(self.statements).mutate()

    def crossover(self, other: ExecutionBlock) -> None:
        max_index: int = min(len(self.statements), len(other.statements))
        if max_index <= 1:
            raise ValueError(f'At least one of the offsprings is too short for crossover!')

        start_index: int = randint(1, max_index - 1)

        self.statements[start_index: max_index], other.statements[start_index: max_index] = \
            other.statements[start_index: max_index], self.statements[start_index: max_index]

    def __str__(self) -> str:
        tabs: str = '\t' * (self.meta.depth + 1)
        statements_print = '\n'.join([f'{tabs}{statement}' for statement in self.statements])
        return f'{{\n{statements_print}\n{tabs[1:]}}}'

    def __len__(self) -> int:
        return sum([len(child) for child in self.statements])


@dataclass(slots=True)
class Assigment(Mutable, RestrictedRandomize):
    name: VariableNameToken
    assigment_value: AssigmentValueType

    @classmethod
    def from_random(cls, meta: Metadata) -> Assigment:
        constructor = choice(cls.generate_choices(meta))
        value: AssigmentValueType = constructor.from_random(Metadata(meta.variables_scope, 0))

        match constructor:
            case self_namespace.Expression:
                name: VariableNameToken = VariableNameToken(meta.get_random_name('int'))

            case self_namespace.Condition | _:
                name: VariableNameToken = VariableNameToken(meta.get_random_name('bool'))

        return cls(meta, name, value)

    @classmethod
    def generate_choices(cls, meta: Metadata) -> list:
        output: list = []
        if meta.has_boolean_variables():
            output.extend([
                Condition,
            ])

        if meta.has_integer_variables():
            output.extend([
                Expression,
            ])

        return output

    def mutate(self) -> None:
        pass

    def __str__(self) -> str:
        return f'{self.name} = {self.assigment_value};'

    def __len__(self) -> int:
        return len(self.assigment_value) + 1


@dataclass(slots=True)
class IfStatement(Mutable, RestrictedRandomize):
    condition: Condition
    body: ExecutionBlock
    else_statement: Optional[ExecutionBlock]

    @classmethod
    def from_random(cls, meta: Metadata) -> IfStatement:
        condition: Condition = Condition.from_random(Metadata(meta.variables_scope, 0))
        body: ExecutionBlock = ExecutionBlock.from_random(Metadata(deepcopy(meta.variables_scope), meta.depth + 1))
        table_of_choices: list = cls.generate_choices(meta)

        match choice(table_of_choices):
            case self_namespace.ExecutionBlock as option:
                else_statement: Optional[ExecutionBlock] = option.from_random(
                    Metadata(deepcopy(meta.variables_scope), meta.depth + 1))

            case _:
                else_statement: Optional[ExecutionBlock] = None

        return cls(meta, condition, body, else_statement)

    @classmethod
    def generate_choices(cls, meta: Metadata) -> list:
        match meta.method:
            case GenerationMethod.FULL:
                return [ExecutionBlock]

            case GenerationMethod.GROW:
                return [ExecutionBlock, None]

    def mutate(self) -> None:
        pass

    def __str__(self) -> str:
        base: str = f'if ({self.condition}) {self.body}'

        if self.else_statement is not None:
            return f'{base} else {self.else_statement}'

        return base

    def __len__(self) -> int:
        base_length: int = len(self.condition) + len(self.body)

        if self.else_statement is not None:
            return base_length + len(self.else_statement)

        return base_length


@dataclass(slots=True)
class LoopStatement(Mutable, RestrictedRandomize):
    condition: Condition
    body: ExecutionBlock

    @classmethod
    def from_random(cls, meta: Metadata) -> LoopStatement:
        condition: Condition = Condition.from_random(Metadata(meta.variables_scope, 0))
        body: ExecutionBlock = ExecutionBlock.from_random(Metadata(deepcopy(meta.variables_scope), meta.depth + 1))

        return cls(meta, condition, body)

    def mutate(self) -> None:
        pass

    def __str__(self):
        return f'while ({self.condition}) {self.body}'

    def __len__(self):
        return len(self.condition) + len(self.body)


class IOType(Enum):
    READ = 0,
    WRITE = auto()

    def __str__(self):
        return self.name.lower()

    @classmethod
    def from_random(cls, meta: Metadata) -> IOType:
        options: list = [
            cls.WRITE,
        ]

        if not meta.is_empty():
            options.extend([
                cls.READ,
            ])

        return choice(options)

    @classmethod
    def get_opposite(cls, io_type: IOType) -> IOType:
        if io_type == cls.READ:
            return cls.WRITE

        return cls.READ


@dataclass(slots=True)
class IOStatement(Mutable, RestrictedRandomize):
    io_type: IOType
    body: VariableNameToken | Condition | Expression

    @classmethod
    def from_random(cls, meta: Metadata) -> IOStatement:
        io_type: IOType = IOType.from_random(meta)
        match io_type:
            case IOType.READ:
                body: VariableNameToken = VariableNameToken(meta.get_random_name())

            case IOType.WRITE | _:
                body: Condition | Expression = \
                    choice((Condition, Expression)).from_random(Metadata(meta.variables_scope, 0))

        return cls(meta, io_type, body)

    def mutate(self) -> None:
        pass

    def __str__(self) -> str:
        return f'{self.io_type}({self.body});'

    def __len__(self) -> int:
        match self.io_type:
            case IOType.READ:
                return 2

            case IOType.WRITE | _:
                return len(self.body) + 1


@dataclass(slots=True)
class IntegerDeclaration(Mutable, RestrictedRandomize):
    name: VariableNameToken
    expression: Expression

    @classmethod
    def from_random(cls, meta: Metadata) -> IntegerDeclaration:
        name: VariableNameToken = VariableNameToken.from_random()
        expression: Expression = Expression.from_random(Metadata(meta.variables_scope, 0))

        meta.variables_scope[name.value] = 'int'

        return cls(meta, name, expression)

    def mutate(self) -> None:
        pass

    def __str__(self) -> str:
        return f'int {self.name} = {self.expression};'

    def __len__(self) -> int:
        return len(self.expression) + 1


@dataclass(slots=True)
class BooleanDeclaration(Mutable, RestrictedRandomize):
    name: VariableNameToken
    condition: Condition

    @classmethod
    def from_random(cls, meta: Metadata) -> BooleanDeclaration:
        name: VariableNameToken = VariableNameToken.from_random()
        condition: Condition = Condition.from_random(Metadata(meta.variables_scope, 0))

        meta.variables_scope[name.value] = 'bool'

        return cls(meta, name, condition)

    def mutate(self) -> None:
        pass

    def __str__(self) -> str:
        return f'bool {self.name} = {self.condition};'

    def __len__(self) -> int:
        return len(self.condition) + 1


@dataclass(slots=True)
class Condition(Mutable, RestrictedRandomize):
    body: ConditionType

    @classmethod
    def from_random(cls, meta: Metadata) -> Condition:
        table_of_choices: list = cls.generate_choices(meta)

        match choice(table_of_choices):
            case (left, operation, right):
                deeper_meta: Metadata = Metadata(meta.variables_scope, meta.depth + 1)
                return cls(meta, (left.from_random(deeper_meta), operation, right.from_random(deeper_meta)))

            case self_namespace.Condition as option:
                return cls(meta, option.from_random(Metadata(meta.variables_scope, meta.depth + 1)))

            case self_namespace.VariableNameToken:
                return cls(meta, VariableNameToken(meta.get_random_name('bool')))

            case self_namespace.BooleanToken as option:
                return cls(meta, option.from_random())

    @classmethod
    def generate_choices(cls, meta: Metadata) -> list:
        match meta.method:
            case GenerationMethod.FULL:
                if meta.is_depth_in_limits():
                    return [
                        (Expression, choice(('==', '!=', '>', '<', '>=', '<=')), Expression),
                        (Condition, choice(('&&', '||')), Condition),
                        Condition,
                    ]

                output: list = [
                    BooleanToken
                ]
                if not meta.is_empty() and meta.has_boolean_variables():
                    output.extend([
                        VariableNameToken,
                    ])

                return output

            case GenerationMethod.GROW:
                output: list = [
                    BooleanToken
                ]
                if not meta.is_empty() and meta.has_boolean_variables():
                    output.extend([
                        VariableNameToken,
                    ])

                if meta.is_depth_in_limits():
                    output.extend([
                        (Expression, choice(('==', '!=', '>', '<', '>=', '<=')), Expression),
                        (Condition, choice(('&&', '||')), Condition),
                        Condition,
                    ])

                return output

    def mutate(self) -> None:
        pass

    def __str__(self) -> str:
        match self.body:
            case (left, operation, right):
                return f'({left} {operation} {right})'

            case Condition() as value:
                return f'!({str(value)})'

            case _ as value:
                return str(value)

    def __len__(self) -> int:
        match self.body:
            case (left, _, right):
                return len(left) + len(right) + 1

            case Condition() as value:
                return len(value) + 1

            case _:
                return 1


@dataclass(slots=True)
class Expression(Mutable, RestrictedRandomize):
    body: ExpressionType

    @classmethod
    def from_random(cls, meta: Metadata) -> Expression:
        table_of_choices: list = cls.generate_choices(meta)

        match choice(table_of_choices):
            case (right, operation, left):
                deeper_meta: Metadata = Metadata(meta.variables_scope, meta.depth + 1)
                return cls(meta, (left.from_random(deeper_meta), operation, right.from_random(deeper_meta)))

            case self_namespace.VariableNameToken:
                return cls(meta, VariableNameToken(meta.get_random_name('int')))

            case self_namespace.IntegerToken as option:
                return cls(meta, option.from_random())

    @classmethod
    def generate_choices(cls, meta: Metadata) -> list:
        match meta.method:
            case GenerationMethod.FULL:
                if meta.is_depth_in_limits():
                    return [
                        (Expression, choice(('+', '-', '*', '/')), Expression),
                    ]

                output: list = [IntegerToken]
                if not meta.is_empty() and meta.has_integer_variables():
                    output.extend([
                        VariableNameToken,
                    ])

                return output

            case GenerationMethod.GROW:
                output: list = [
                    IntegerToken,
                ]
                if not meta.is_empty() and meta.has_integer_variables():
                    output.extend([
                        VariableNameToken,
                    ])

                if meta.is_depth_in_limits():
                    output.extend([
                        (Expression, choice(('+', '-', '*', '/')), Expression),
                    ])

                return output

    def mutate(self) -> None:
        pass

    def __str__(self) -> str:
        match self.body:
            case (left, operation, right):
                return f'({left} {operation} {right})'

            case _ as value:
                return str(value)

    def __len__(self) -> int:
        match self.body:
            case (left, _, right):
                return len(left) + len(right) + 1

            case _:
                return 1


ExpressionType = Union[Tuple[Expression, str, Expression], VariableNameToken, IntegerToken]
ConditionType = Union[
    Tuple[Condition, str, Condition], Tuple[Expression, str, Expression], Condition, VariableNameToken, BooleanToken]
StatementBodyTypes = Union[IntegerDeclaration, BooleanDeclaration, Assigment, IfStatement, LoopStatement, IOStatement]
DeclarationTypes = Union[IntegerDeclaration, BooleanDeclaration]
AssigmentValueType = Union[Expression, Condition]

self_namespace = SimpleNamespace(**{
    cls.__name__: cls for _, cls in inspect.getmembers(
        importlib.import_module(__name__),
        inspect.isclass
    )
})
