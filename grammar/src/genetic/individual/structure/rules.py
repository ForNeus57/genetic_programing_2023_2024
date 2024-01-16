from __future__ import annotations

import importlib
import inspect
from dataclasses import dataclass, field
from types import SimpleNamespace
from typing import Union, Optional, Tuple
from random import choice
from enum import Enum, auto
from copy import deepcopy

from src.genetic.individual.interfaces.node_types import Rule
from src.genetic.individual.interfaces.randomize import RestrictedRandomize, Metadata, VariableNameToken, \
    IntegerToken, BooleanToken, RandomGenerationMethod

from src.genetic.individual.limiters.limiters import Limiter
from src.genetic.interpreter.variables import Variable


@dataclass(slots=True, frozen=True)
class Program(Rule, RestrictedRandomize):
    body: ExecutionBlock

    @classmethod
    def from_random(cls, meta: Metadata) -> Program:
        block = ExecutionBlock.from_random(meta)
        return cls(meta, block)

    def mutate(self) -> None:
        pass

    def crossover(self, other: Program) -> None:
        pass

    def __str__(self) -> str:
        return str(self.body)


@dataclass(slots=True, frozen=True)
class ExecutionBlock(Rule, RestrictedRandomize):
    statements: list[StatementBodyTypes] = field(default_factory=list)

    @classmethod
    def from_random(cls, meta: Metadata) -> ExecutionBlock:
        body: list[StatementBodyTypes] = []
        limiter: Limiter = meta.limiter()

        statement = cls.generate_random_body_element(meta)
        child_meta: Metadata = statement.meta
        body.append(statement)

        while limiter.allow():
            statement = cls.generate_random_body_element(child_meta)
            child_meta = statement.meta
            body.append(statement)

        return cls(meta, body)

    @classmethod
    def generate_random_body_element(cls, meta: Metadata) -> StatementBodyTypes:
        table_of_choices: list = cls.generate_choices(meta)

        match choice(table_of_choices):
            case namespace.IfStatement | namespace.LoopStatement as option:
                return option.from_random(Metadata(meta.variables_scope, meta.depth + 1))

            case _ as option:
                return option.from_random(meta)

    @classmethod
    def generate_choices(cls, meta: Metadata) -> list:
        match meta.method:
            case RandomGenerationMethod.FULL:
                if meta.is_depth_in_limits():
                    return [
                        IfStatement,
                        LoopStatement,
                    ]

                output: list = [
                    VarDeclaration,
                ]
                if not meta.is_empty():
                    output.extend([
                        Assigment,
                        IOStatement,
                    ])


                return output

            case RandomGenerationMethod.GROW:
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


    def mutate(self) -> None:
        pass

    def crossover(self, other: ExecutionBlock) -> None:
        pass

    def __str__(self) -> str:
        tabs: str = '\t' * (self.meta.depth + 1)
        statements_print = '\n'.join([f'{tabs}{statement}' for statement in self.statements])
        return f'{{\n{statements_print}\n{tabs[2:]}}}\n'


@dataclass(slots=True, frozen=True)
class VarDeclaration(Rule, RestrictedRandomize):
    is_constant: bool
    declaration: DeclarationTypes

    @classmethod
    def from_random(cls, meta: Metadata) -> VarDeclaration:
        is_constant = choice([True, False])
        declaration: DeclarationTypes = choice([IntegerDeclaration, BooleanDeclaration]).from_random(Metadata(meta.variables_scope, meta.depth + 1))

        meta.variables_scope[declaration.name.value].is_constant = is_constant

        return cls(meta, is_constant, declaration)

    def mutate(self) -> None:
        pass

    def crossover(self, other: VarDeclaration) -> None:
        pass

    def __str__(self):
        return f'{"const " if self.is_constant else ""}{self.declaration};'


@dataclass(slots=True, frozen=True)
class Assigment(Rule, RestrictedRandomize):
    name: VariableNameToken
    assigment_value: AssigmentValueType

    @classmethod
    def from_random(cls, meta: Metadata) -> Assigment:
        constructor = choice(cls.generate_choices(meta))
        value: AssigmentValueType = constructor.from_random(Metadata(meta.variables_scope, 0))  # Don't forget Validation...

        match constructor:
            case namespace.Expression:
                name: VariableNameToken = VariableNameToken(meta.get_random_name('int'))

            case namespace.Condition:
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

    def crossover(self, other: Assigment) -> None:
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
        condition: Condition = Condition.from_random(Metadata(meta.variables_scope, 0))
        body: ExecutionBlock = ExecutionBlock.from_random(Metadata(deepcopy(meta.variables_scope), meta.depth + 1))
        table_of_choices: list = cls.generate_choices(meta)

        match choice(table_of_choices):
            case namespace.ExecutionBlock as option:
                else_statement: Optional[ExecutionBlock] = option.from_random(
                    Metadata(deepcopy(meta.variables_scope), meta.depth + 1))

            case _:
                else_statement: Optional[ExecutionBlock] = None

        return cls(meta, condition, body, else_statement)

    @classmethod
    def generate_choices(cls, meta: Metadata) -> list:
        match meta.method:
            case RandomGenerationMethod.FULL:
                return [ExecutionBlock]

            case RandomGenerationMethod.GROW:
                return [ExecutionBlock, None]


    def mutate(self) -> None:
        pass

    def crossover(self, other: IfStatement) -> None:
        pass

    def __str__(self):
        base: str = f'if ({self.condition}) {self.body}'

        if self.else_statement is not None:
            indentation: str = '\t' * self.meta.depth
            return base + f'{indentation}else {self.else_statement}'

        return base


@dataclass(slots=True, frozen=True)
class LoopStatement(Rule, RestrictedRandomize):
    condition: Condition
    body: ExecutionBlock

    @classmethod
    def from_random(cls, meta: Metadata) -> LoopStatement:
        condition: Condition = Condition.from_random(Metadata(meta.variables_scope, 0))
        body: ExecutionBlock = ExecutionBlock.from_random(Metadata(deepcopy(meta.variables_scope), meta.depth + 1))

        return cls(meta, condition, body)

    def mutate(self) -> None:
        pass

    def crossover(self, other: LoopStatement) -> None:
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
        name: VariableNameToken = VariableNameToken(meta.get_random_name())

        return cls(meta, io_type, name)

    def mutate(self) -> None:
        pass

    def crossover(self, other: IOStatement) -> None:
        pass

    def __str__(self):
        return f'{self.io_type} ({self.name});'


@dataclass(slots=True, frozen=True)
class IntegerDeclaration(Rule, RestrictedRandomize):
    name: VariableNameToken
    expression: Expression

    @classmethod
    def from_random(cls, meta: Metadata) -> IntegerDeclaration:
        name: VariableNameToken = VariableNameToken.from_random()
        expression: Expression = Expression.from_random(Metadata(meta.variables_scope, 0))

        meta.variables_scope[name.value] = Variable(None, 'int', None)

        return cls(meta, name, expression)

    def mutate(self) -> None:
        pass

    def crossover(self, other: IntegerDeclaration) -> None:
        pass

    def __str__(self):
        base: str = f'int {self.name}'
        if self.expression is not None:
            return base + f' = {self.expression}'

        return base


@dataclass(slots=True, frozen=True)
class BooleanDeclaration(Rule, RestrictedRandomize):
    name: VariableNameToken
    condition: Condition

    @classmethod
    def from_random(cls, meta: Metadata) -> BooleanDeclaration:
        name: VariableNameToken = VariableNameToken.from_random()
        condition: Condition = Condition.from_random(Metadata(meta.variables_scope, 0))

        meta.variables_scope[name.value] = Variable(None, 'bool', None)

        return cls(meta, name, condition)

    def mutate(self) -> None:
        pass

    def crossover(self, other: BooleanDeclaration) -> None:
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
                return cls(meta, (left.from_random(Metadata(meta.variables_scope, meta.depth + 1)), operation,
                                  right.from_random(Metadata(meta.variables_scope, meta.depth + 1))))

            case namespace.Condition as option:
                return cls(meta, option.from_random(Metadata(meta.variables_scope, meta.depth + 1)))

            case namespace.VariableNameToken:
                return cls(meta, VariableNameToken(meta.get_random_name('bool')))

            case namespace.BooleanToken as option:
                return cls(meta, option.from_random())

    @classmethod
    def generate_choices(cls, meta: Metadata) -> list:
        match meta.method:
            case RandomGenerationMethod.FULL:
                if meta.is_depth_in_limits():
                    return [
                        (Expression, choice(['==', '!=', '>', '<', '>=', '<=']), Expression),
                        (Condition, choice(['&&', '||', '^']), Condition),
                        Condition,
                    ]

                output: list = [BooleanToken]
                if not meta.is_empty() and meta.has_boolean_variables():
                    output.extend([
                        VariableNameToken,
                    ])

                return output

            case RandomGenerationMethod.GROW:
                output: list = [
                    BooleanToken
                ]
                if not meta.is_empty() and meta.has_boolean_variables():
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

    def mutate(self) -> None:
        pass

    def crossover(self, other: Condition) -> None:
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
                return cls(meta, (left.from_random(Metadata(meta.variables_scope, meta.depth + 1)), operation,
                                  right.from_random(Metadata(meta.variables_scope, meta.depth + 1))))

            case namespace.VariableNameToken:
                return cls(meta, VariableNameToken(meta.get_random_name('int')))

            case namespace.IntegerToken as option:
                return cls(meta, option.from_random())

    @classmethod
    def generate_choices(cls, meta: Metadata) -> list:
        match meta.method:
            case RandomGenerationMethod.FULL:
                if meta.is_depth_in_limits():
                    return [
                        (Expression, choice(['+', '-', '*', '/']), Expression),
                    ]

                output: list = [IntegerToken]
                if not meta.is_empty() and meta.has_integer_variables():
                    output.extend([
                        VariableNameToken,
                    ])

                return output

            case RandomGenerationMethod.GROW:
                output: list = [
                    IntegerToken,
                ]
                if not meta.is_empty() and meta.has_integer_variables():
                    output.extend([
                        VariableNameToken,
                    ])

                if meta.is_depth_in_limits():
                    output.extend([
                        (Expression, choice(['+', '-', '*', '/']), Expression),
                    ])

                return output

    def mutate(self) -> None:
        pass

    def crossover(self, other: Expression) -> None:
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
