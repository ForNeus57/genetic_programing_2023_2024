from __future__ import annotations

import importlib
import inspect
from dataclasses import dataclass, field
from types import SimpleNamespace
from typing import Union, Optional, Tuple
from random import choice, random, randint
from enum import Enum, auto
from copy import deepcopy

from src.genetic.individual.interfaces.node_types import Rule, RestrictedRandomize
from src.genetic.individual.structure.tokens import Metadata, VariableNameToken, \
    IntegerToken, BooleanToken, GenerationMethod

from src.genetic.individual.limiters.limiters import Limiter
from src.genetic.interpreter.variables import Variable


@dataclass(slots=True)
class Program(Rule, RestrictedRandomize):
    body: ExecutionBlock

    @classmethod
    def from_random(cls, meta: Metadata) -> Program:
        block = ExecutionBlock.from_random(meta)
        return cls(meta, block)

    def mutate(self) -> None:
        self.body.mutate()

    def crossover(self, other: Program) -> None:
        self.body.crossover(other.body)

    def __str__(self) -> str:
        return str(self.body)


@dataclass(slots=True)
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
            statement = cls.generate_random_body_element(Metadata(child_meta.variables_scope, meta.depth + 1))
            child_meta = statement.meta
            body.append(statement)

        return cls(meta, body)

    @classmethod
    def generate_random_body_element(cls, meta: Metadata) -> StatementBodyTypes:
        table_of_choices: list = cls.generate_choices(meta)

        match choice(table_of_choices):
            case self_namespace.IfStatement | self_namespace.LoopStatement as option:
                return option.from_random(Metadata(meta.variables_scope, meta.depth + 1))

            case _ as option:
                return option.from_random(meta)

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
                ]
                if not meta.is_empty():
                    output.extend([
                        Assigment,
                        IOStatement,
                    ])

                return output

            case GenerationMethod.GROW:
                output: list = [
                    IntegerDeclaration,
                    BooleanDeclaration,
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
        for index, statement in enumerate(self.statements):
            if random() < Rule.mutation_from_start_probability:
                self.statements[index] = self.generate_random_body_element(statement.meta)
            elif random() < Rule.mutation_node_probability:
                statement.mutate()

        self.statements.append(self.generate_random_body_element(self.meta))

    def crossover(self, other: ExecutionBlock) -> None:
        self_length, other_length = len(self.statements), len(other.statements)
        self_random_length, other_random_length = randint(0, self_length - 1), randint(0, other_length - 1)
        self_start_index, other_start_index = randint(0, self_length - self_random_length - 1), randint(0, other_length - other_random_length - 1)

        self_statements_copy = deepcopy(self.statements)
        other_statements_copy = deepcopy(other.statements)

        self.statements[self_start_index: self_start_index + self_random_length] = \
            other_statements_copy[other_start_index: other_start_index + other_random_length]

        other.statements[other_start_index: other_start_index + other_random_length] = \
            self_statements_copy[self_start_index: self_start_index + self_random_length]

    def __str__(self) -> str:
        tabs: str = '\t' * (self.meta.depth + 1)
        statements_print = '\n'.join([f'{tabs}{statement}' for statement in self.statements])
        return f'{{\n{statements_print}\n{tabs[2:]}}}\n'


@dataclass(slots=True)
class Assigment(Rule, RestrictedRandomize):
    name: VariableNameToken
    assigment_value: AssigmentValueType

    @classmethod
    def from_random(cls, meta: Metadata) -> Assigment:
        constructor = cls.generate_choices(meta)
        value: AssigmentValueType = constructor.from_random(Metadata(meta.variables_scope, 0))

        match choice(constructor):
            case self_namespace.Expression:
                name: VariableNameToken = VariableNameToken(meta.get_random_name('int'))

            case self_namespace.Condition:
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
        self.name = VariableNameToken(self.meta.get_random_name())

        if random() < Rule.mutation_from_start_probability:
            self.assigment_value = choice(self.generate_choices(self.meta)).from_random(
                Metadata(self.meta.variables_scope, 0))
        elif random() < Rule.mutation_node_probability:
            self.assigment_value.mutate()

    def crossover(self, other: Assigment) -> None:
        self.name, other.name = other.name, self.name
        if type(self.assigment_value) is type(other.assigment_value):
            self.assigment_value.crossover(other.assigment_value)

    def __str__(self):
        return f'{self.name} = {self.assigment_value};'


@dataclass(slots=True)
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
        if random() < Rule.mutation_from_start_probability:
            self.condition = Condition.from_random(Metadata(self.meta.variables_scope, 0))
        elif random() < Rule.mutation_node_probability:
            self.condition.mutate()

        if random() < Rule.mutation_from_start_probability:
            self.body = ExecutionBlock.from_random(Metadata(deepcopy(self.meta.variables_scope), self.meta.depth + 1))
        elif random() < Rule.mutation_node_probability:
            self.body.mutate()

        if self.else_statement is None and random() < Rule.mutation_from_start_probability:
            self.else_statement = ExecutionBlock.from_random(
                Metadata(deepcopy(self.meta.variables_scope), self.meta.depth + 1))
        elif self.else_statement is not None and random() < Rule.mutation_node_probability:
            self.else_statement.mutate()

    def crossover(self, other: IfStatement) -> None:
        self.condition, other.condition = other.condition, self.condition
        self.body.crossover(other.body)

        if self.else_statement is None and other.else_statement is not None:
            self.else_statement = other.else_statement
        elif self.else_statement is not None and other.else_statement is None:
            other.else_statement = self.else_statement

    def __str__(self):
        base: str = f'if ({self.condition}) {self.body}'

        if self.else_statement is not None:
            indentation: str = '\t' * self.meta.depth
            return base + f'{indentation}else {self.else_statement}'

        return base


@dataclass(slots=True)
class LoopStatement(Rule, RestrictedRandomize):
    condition: Condition
    body: ExecutionBlock

    @classmethod
    def from_random(cls, meta: Metadata) -> LoopStatement:
        condition: Condition = Condition.from_random(Metadata(meta.variables_scope, 0))
        body: ExecutionBlock = ExecutionBlock.from_random(Metadata(deepcopy(meta.variables_scope), meta.depth + 1))

        return cls(meta, condition, body)

    def mutate(self) -> None:
        if random() < Rule.mutation_from_start_probability:
            self.condition = Condition.from_random(Metadata(self.meta.variables_scope, 0))
        elif random() < Rule.mutation_node_probability:
            self.condition.mutate()

        if random() < Rule.mutation_from_start_probability:
            self.body = ExecutionBlock.from_random(Metadata(deepcopy(self.meta.variables_scope), self.meta.depth + 1))
        elif random() < Rule.mutation_node_probability:
            self.body.mutate()

    def crossover(self, other: LoopStatement) -> None:
        self.condition, other.condition = other.condition, self.condition
        self.body.crossover(other.body)

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

    @classmethod
    def get_opposite(cls, io_type: IOType) -> IOType:
        if io_type == cls.READ:
            return cls.WRITE

        return cls.READ


@dataclass(slots=True)
class IOStatement(Rule, RestrictedRandomize):
    io_type: IOType
    name: VariableNameToken

    @classmethod
    def from_random(cls, meta: Metadata) -> IOStatement:
        io_type: IOType = IOType.from_random()
        name: VariableNameToken = VariableNameToken(meta.get_random_name())

        return cls(meta, io_type, name)

    def mutate(self) -> None:
        IOType.get_opposite(self.io_type)

        if random() < Rule.mutation_node_probability:
            self.name = VariableNameToken(self.meta.get_random_name())

    def crossover(self, other: IOStatement) -> None:
        self.io_type, other.io_type = other.io_type, self.io_type

    def __str__(self):
        return f'{self.io_type} ({self.name});'


@dataclass(slots=True)
class IntegerDeclaration(Rule, RestrictedRandomize):
    name: VariableNameToken
    expression: Expression

    @classmethod
    def from_random(cls, meta: Metadata) -> IntegerDeclaration:
        name: VariableNameToken = VariableNameToken.from_random()
        expression: Expression = Expression.from_random(Metadata(meta.variables_scope, 0))

        meta.variables_scope[name.value] = Variable('int', None)

        return cls(meta, name, expression)

    def mutate(self) -> None:
        if random() < Rule.mutation_node_probability:
            self.name = VariableNameToken(self.meta.get_random_name())

        if random() < Rule.mutation_node_probability:
            self.expression.mutate()

    def crossover(self, other: IntegerDeclaration) -> None:
        self.expression, other.expression = other.expression, self.expression

    def __str__(self):
        base: str = f'int {self.name}'
        if self.expression is not None:
            return base + f' = {self.expression}'

        return base


@dataclass(slots=True)
class BooleanDeclaration(Rule, RestrictedRandomize):
    name: VariableNameToken
    condition: Condition

    @classmethod
    def from_random(cls, meta: Metadata) -> BooleanDeclaration:
        name: VariableNameToken = VariableNameToken.from_random()
        condition: Condition = Condition.from_random(Metadata(meta.variables_scope, 0))

        meta.variables_scope[name.value] = Variable('bool', None)

        return cls(meta, name, condition)

    def mutate(self) -> None:
        if random() < Rule.mutation_node_probability:
            self.name = VariableNameToken(self.meta.get_random_name())

        if random() < Rule.mutation_node_probability:
            self.condition.mutate()

    def crossover(self, other: BooleanDeclaration) -> None:
        self.condition, other.condition = other.condition, self.condition

    def __str__(self):
        base: str = f'bool {self.name}'
        if self.condition is not None:
            return base + f' = {self.condition}'

        return base


@dataclass(slots=True)
class Condition(Rule, RestrictedRandomize):
    body: ConditionType

    @classmethod
    def from_random(cls, meta: Metadata) -> Condition:
        table_of_choices: list = cls.generate_choices(meta)

        match choice(table_of_choices):
            case (left, operation, right):
                return cls(meta, (left.from_random(Metadata(meta.variables_scope, meta.depth + 1)), operation,
                                  right.from_random(Metadata(meta.variables_scope, meta.depth + 1))))

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
                        (Expression, choice(['==', '!=', '>', '<', '>=', '<=']), Expression),
                        (Condition, choice(['&&', '||']), Condition),
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
                        (Expression, choice(['==', '!=', '>', '<', '>=', '<=']), Expression),
                        (Condition, choice(['&&', '||']), Condition),
                        Condition,
                    ])

                return output

    def mutate(self) -> None:
        if random() < Rule.mutation_node_probability:
            self.body = Condition.from_random(self.meta).body

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


@dataclass(slots=True)
class Expression(Rule, RestrictedRandomize):
    body: ExpressionType

    @classmethod
    def from_random(cls, meta: Metadata) -> Expression:
        table_of_choices: list = cls.generate_choices(meta)

        match choice(table_of_choices):
            case (right, operation, left):
                return cls(meta, (left.from_random(Metadata(meta.variables_scope, meta.depth + 1)), operation,
                                  right.from_random(Metadata(meta.variables_scope, meta.depth + 1))))

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
                        (Expression, choice(['+', '-', '*', '/']), Expression),
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
                        (Expression, choice(['+', '-', '*', '/']), Expression),
                    ])

                return output

    def mutate(self) -> None:
        if random() < Rule.mutation_node_probability:
            self.body = Expression.from_random(self.meta).body

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
StatementBodyTypes = Union[IntegerDeclaration, BooleanDeclaration, Assigment, IfStatement, LoopStatement, IOStatement]
DeclarationTypes = Union[IntegerDeclaration, BooleanDeclaration]
AssigmentValueType = Union[Expression, Condition]

self_namespace = SimpleNamespace(**{
    cls.__name__: cls for _, cls in inspect.getmembers(
        importlib.import_module(__name__),
        inspect.isclass
    )
})
