from __future__ import annotations

import importlib
import inspect
from dataclasses import dataclass, field
from types import SimpleNamespace
from typing import Union, Optional, Tuple
from random import random, choice
from enum import Enum, auto

from src.genetic.individual.interfaces.node_types import Rule
from src.genetic.individual.probability.exponential_probability import ExponentialProbability
from src.genetic.individual.interfaces.randomize import Randomize, RestrictedRandomize, Metadata, VariableNameToken, \
    IntegerToken, BooleanToken


@dataclass(slots=True, frozen=True)
class Program(Rule, Randomize):
    body: ExecutionBlock

    @classmethod
    def from_random(cls) -> Program:
        meta: Metadata = Metadata()
        block = ExecutionBlock.from_random(meta)
        return cls(block)

    def mutate(self) -> Program:
        pass

    def crossover(self, other: Program) -> Program:
        pass

    def __str__(self) -> str:
        return str(self.body)


@dataclass(slots=True, frozen=True)
class ExecutionBlock(Rule, RestrictedRandomize):
    statements: list[Statement] = field(default_factory=list)

    @classmethod
    def from_random(cls, meta: Metadata) -> ExecutionBlock:
        body: list[Statement] = []
        probability: ExponentialProbability = ExponentialProbability()
        first_statement = Statement.from_random(meta)
        child_meta: Metadata = first_statement.meta
        body.append(first_statement)

        while next(probability) > random():
            statement: Statement = Statement.from_random(child_meta)
            child_meta = statement.meta
            body.append(statement)

        return cls(meta, body)

    def mutate(self) -> ExecutionBlock:
        pass

    def crossover(self, other: ExecutionBlock) -> ExecutionBlock:
        pass

    def __str__(self) -> str:
        tabs: str = '\t' * self.meta.depth
        statements_print = '\n'.join([f'{tabs}{statement}' for statement in self.statements])
        return f'{{\n{statements_print}\n{tabs[2:]}}}\n'


@dataclass(slots=True, frozen=True)
class Statement(Rule, RestrictedRandomize):
    body: StatementBodyTypes

    @classmethod
    def from_random(cls, meta: Metadata) -> Statement:
        table_of_choices: list = cls.generate_choices(meta)

        match choice(table_of_choices):
            case namespace.IfStatement | namespace.LoopStatement as option:
                body: StatementBodyTypes = option.from_random(Metadata(meta.variables_scope, meta.depth + 1))

            case _ as option:
                body: StatementBodyTypes = option.from_random(meta)

        return cls(meta, body)

    @classmethod
    def generate_choices(cls, meta: Metadata) -> list:
        output: list = [
            VarDeclaration,
        ]
        if not meta.is_empty():
            output.extend([
                Assigment,
                IOStatement
            ])

        if meta.is_depth_in_limits():
            output.extend([
                IfStatement,
                LoopStatement,
            ])

        return output

    def mutate(self) -> Statement:
        pass

    def crossover(self, other: Statement) -> Statement:
        pass

    def __str__(self):
        return str(self.body)


@dataclass(slots=True, frozen=True)
class VarDeclaration(Rule, RestrictedRandomize):
    is_constant: bool
    declaration: DeclarationTypes

    @classmethod
    def from_random(cls, meta: Metadata) -> VarDeclaration:
        is_constant = choice([True, False])
        declaration: DeclarationTypes = choice([IntegerDeclaration, BooleanDeclaration]).from_random(Metadata(meta.variables_scope, meta.depth + 1))
        # meta.variables_scope.add(declaration.name)  # Not sure if needed

        return cls(meta, is_constant, declaration)

    def mutate(self) -> VarDeclaration:
        pass

    def crossover(self, other: VarDeclaration) -> VarDeclaration:
        pass

    def __str__(self):
        return f'{"const " if self.is_constant else ""}{self.declaration};'


@dataclass(slots=True, frozen=True)
class Assigment(Rule, RestrictedRandomize):
    name: VariableNameToken
    assigment_value: AssigmentValueType

    @classmethod
    def from_random(cls, meta: Metadata) -> Assigment:
        name: VariableNameToken = meta.get_random_name()
        value: AssigmentValueType = choice([Expression, Condition]).from_random(Metadata(meta.variables_scope, meta.depth + 1))  # Don't forget Validation...

        return cls(meta, name, value)

    def mutate(self) -> Assigment:
        pass

    def crossover(self, other: Assigment) -> Assigment:
        pass

    def __str__(self):
        return f'{self.name} = {self.assigment_value};'


@dataclass(slots=True, frozen=True)
class IfStatement(Rule, RestrictedRandomize):
    condition: Condition
    body: ExecutionBlock
    else_statement: Optional[ExecutionBlock]

    @classmethod
    def from_random(cls, meta: Metadata) -> IfStatement:
        condition: Condition = Condition.from_random(Metadata(meta.variables_scope, meta.depth + 1))
        body: ExecutionBlock = ExecutionBlock.from_random(Metadata(meta.variables_scope, meta.depth + 1))
        table_of_choices: list = [ExecutionBlock, None]

        match choice(table_of_choices):
            case namespace.ExecutionBlock as option:
                else_statement: Optional[ExecutionBlock] = option.from_random(Metadata(meta.variables_scope, meta.depth + 1))

            case _:
                else_statement: Optional[ExecutionBlock] = None

        return cls(meta, condition, body, else_statement)

    def mutate(self) -> IfStatement:
        pass

    def crossover(self, other: IfStatement) -> IfStatement:
        pass

    def __str__(self):
        base: str = f'if ({self.condition}) {self.body}'

        if self.else_statement is not None:
            indentation: str = '\t' * (self.meta.depth - 1)
            return base + f'{indentation} else {self.else_statement}'

        return base


@dataclass(slots=True, frozen=True)
class LoopStatement(Rule, RestrictedRandomize):
    condition: Condition
    body: ExecutionBlock

    @classmethod
    def from_random(cls, meta: Metadata) -> LoopStatement:
        condition: Condition = Condition.from_random(Metadata(meta.variables_scope, meta.depth + 1))
        body: ExecutionBlock = ExecutionBlock.from_random(Metadata(meta.variables_scope, meta.depth + 1))

        return cls(meta, condition, body)

    def mutate(self) -> LoopStatement:
        pass

    def crossover(self, other: LoopStatement) -> LoopStatement:
        pass

    def __str__(self):
        return f'while ({self.condition}) {self.body}'


class IOType(Enum):
    READ = 0,
    WRITE = auto()

    def __str__(self):
        return self.name.lower()

    @classmethod
    def from_random(cls) -> IOType:
        return choice(list(cls))


@dataclass(slots=True, frozen=True)
class IOStatement(Rule, RestrictedRandomize):
    io_type: IOType
    name: VariableNameToken

    @classmethod
    def from_random(cls, meta: Metadata) -> IOStatement:
        io_type: IOType = IOType.from_random()
        name: VariableNameToken = meta.get_random_name()

        return cls(meta, io_type, name)

    def mutate(self) -> IOStatement:
        pass

    def crossover(self, other: IOStatement) -> IOStatement:
        pass

    def __str__(self):
        return f'{self.io_type} ({self.name});'


@dataclass(slots=True, frozen=True)
class IntegerDeclaration(Rule, RestrictedRandomize):
    name: VariableNameToken
    expression: Optional[Expression]

    @classmethod
    def from_random(cls, meta: Metadata) -> IntegerDeclaration:
        name: VariableNameToken = VariableNameToken.from_random()
        meta.variables_scope.add(name)
        table_of_choices: list = [Expression, None]

        match choice(table_of_choices):
            case namespace.Expression as option:
                expression: Optional[Expression] = option.from_random(Metadata(meta.variables_scope, meta.depth + 1))

            case _:
                expression: Optional[Expression] = None

        return cls(meta, name, expression)

    def mutate(self) -> IntegerDeclaration:
        pass

    def crossover(self, other: IntegerDeclaration) -> IntegerDeclaration:
        pass

    def __str__(self):
        base: str = f'int {self.name}'
        if self.expression is not None:
            return base + f' = {self.expression}'

        return base


@dataclass(slots=True, frozen=True)
class BooleanDeclaration(Rule, RestrictedRandomize):
    name: VariableNameToken
    condition: Optional[Condition]

    @classmethod
    def from_random(cls, meta: Metadata) -> BooleanDeclaration:
        name: VariableNameToken = VariableNameToken.from_random()
        meta.variables_scope.add(name)
        table_of_choices: list = [Condition, None]

        match choice(table_of_choices):
            case namespace.Condition as option:
                condition: Optional[Condition] = option.from_random(Metadata(meta.variables_scope, meta.depth + 1))

            case _:
                condition: Optional[Condition] = None

        return cls(meta, name, condition)

    def mutate(self) -> BooleanDeclaration:
        pass

    def crossover(self, other: BooleanDeclaration) -> BooleanDeclaration:
        pass

    def __str__(self):
        base: str = f'bool {self.name}'
        if self.condition is not None:
            return base + f' = {self.condition}'

        return base


@dataclass(slots=True, frozen=True)
class Condition(Rule, RestrictedRandomize):
    body: ConditionType

    @classmethod
    def from_random(cls, meta: Metadata) -> Condition:
        table_of_choices: list = cls.generate_choices(meta)

        match choice(table_of_choices):
            case (left, operation, right):
                return cls(meta, (left.from_random(Metadata(meta.variables_scope, meta.depth + 1)), operation, right.from_random(Metadata(meta.variables_scope, meta.depth + 1))))

            case namespace.Condition as option:
                return cls(meta, option.from_random(Metadata(meta.variables_scope, meta.depth + 1)))

            case namespace.VariableNameToken:
                return cls(meta, meta.get_random_name())

            case namespace.BooleanToken as option:
                return cls(meta, option.from_random())

    @classmethod
    def generate_choices(cls, meta: Metadata) -> list:
        output: list = [
            BooleanToken
        ]
        if not meta.is_empty():
            output.extend([
                VariableNameToken,
            ])

        if meta.is_depth_in_limits():
            output.extend([
                (Expression, choice(['==', '!=', '>', '<', '>=', '<=']), Expression),
                (Condition, choice(['&&', '||', '^']), Condition),
                Condition,
            ])

        return output

    def mutate(self) -> Condition:
        pass

    def crossover(self, other: Condition) -> Condition:
        pass

    def __str__(self):
        match self.body:
            case (left, operation, right):
                return f'({left} {operation} {right})'

            case Condition() as value:
                return f'!({str(value)})'

            case _ as value:
                return str(value)


@dataclass(slots=True, frozen=True)
class Expression(Rule, RestrictedRandomize):
    body: ExpressionType

    @classmethod
    def from_random(cls, meta: Metadata) -> Expression:
        table_of_choices: list = cls.generate_choices(meta)

        match choice(table_of_choices):
            case (right, operation, left):
                return cls(meta, (left.from_random(Metadata(meta.variables_scope, meta.depth + 1)), operation, right.from_random(Metadata(meta.variables_scope, meta.depth + 1))))

            case namespace.VariableNameToken:
                return cls(meta, meta.get_random_name())

            case namespace.IntegerToken as option:
                return cls(meta, option.from_random())

    @classmethod
    def generate_choices(cls, meta: Metadata) -> list:
        output: list = [
            IntegerToken,
        ]
        if not meta.is_empty():
            output.extend([
                VariableNameToken,
            ])

        if meta.is_depth_in_limits():
            output.extend([
                (Expression, choice(['+', '-', '*', '/']), Expression),
            ])

        return output

    def mutate(self) -> Expression:
        pass

    def crossover(self, other: Expression) -> Expression:
        pass

    def __str__(self):
        match self.body:
            case (left, operation, right):
                return f'({left} {operation} {right})'

            case _ as value:
                return str(value)


ExpressionType = Union[Tuple[Expression, str, Expression], VariableNameToken, IntegerToken]
ConditionType = Union[
    Tuple[Condition, str, Condition], Tuple[Expression, str, Expression], Condition, VariableNameToken, BooleanToken]
StatementBodyTypes = Union[VarDeclaration, Assigment, IfStatement, LoopStatement, IOStatement]
DeclarationTypes = Union[IntegerDeclaration, BooleanDeclaration]
AssigmentValueType = Union[Expression, Condition]

namespace = SimpleNamespace(**{
    cls.__name__: cls for _, cls in inspect.getmembers(
        importlib.import_module(__name__),
        inspect.isclass
    )
})
