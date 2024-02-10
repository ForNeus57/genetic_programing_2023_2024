from __future__ import annotations

import importlib
import inspect
from copy import deepcopy
from dataclasses import dataclass, field
from enum import Enum, auto
from random import choice, randint, random
from types import SimpleNamespace
from typing import Optional, Tuple

from src.genetic.individual.structure.limiters import Limiter
from src.genetic.individual.structure.metadata import Metadata, GenerationMethod
from src.genetic.individual.structure.node_types import Crossover, RestrictedRandomize, Rule
from src.genetic.individual.structure.tokens import VariableNameToken, IntegerToken, BooleanToken
from src.genetic.interpreter.context import InterpreterContext


@dataclass(slots=True)
class Program(Crossover, Rule, RestrictedRandomize):
    body: ExecutionBlock

    @classmethod
    def from_random(cls, meta: Metadata) -> Program:
        block: ExecutionBlock = ExecutionBlock.from_random(meta)
        return cls(meta, block)

    def mutate(self) -> None:
        self.body.mutate()

    def crossover(self, other: Program) -> None:
        self.body.crossover(other.body)

    def visit_commands(self, context: InterpreterContext) -> None:
        self.body.visit(context)

    def __str__(self) -> str:
        return str(self.body)

    def __len__(self) -> int:
        return len(self.body)


@dataclass(slots=True)
class ExecutionBlock(Crossover, Rule, RestrictedRandomize):
    statements: list[StatementBodyTypes] = field(default_factory=list)

    @classmethod
    def from_random(cls, meta: Metadata) -> ExecutionBlock:
        limiter: Limiter = deepcopy(meta.limiter)
        body: list[StatementBodyTypes] = []

        statement: StatementBodyTypes = cls.generate_random_body_element(meta)
        child_meta: Metadata = statement.meta
        body.append(statement)

        statement: StatementBodyTypes = cls.generate_random_body_element(child_meta)
        child_meta: Metadata = statement.meta
        body.append(statement)

        while limiter.allow():
            statement: StatementBodyTypes = cls.generate_random_body_element(child_meta)
            child_meta: Metadata = statement.meta
            body.append(statement)

        return cls(meta, body)

    @classmethod
    def generate_random_body_element(cls, meta: Metadata) -> StatementBodyTypes:
        return choice(cls.generate_choices(meta)).from_random(meta)

    @classmethod
    def generate_choices(cls, meta: Metadata) -> list:
        match meta.method:
            case GenerationMethod.FULL:
                if meta.is_depth_in_limits():
                    return [
                        IfStatement,
                        LoopStatement,
                    ]

                return [
                    Assigment,
                    IOStatement,
                ]

            case GenerationMethod.GROW:
                output: list = [
                    Assigment,
                    IOStatement,
                ]

                if meta.is_depth_in_limits():
                    output.extend([
                        IfStatement,
                        LoopStatement,
                    ])

                return output

    def mutate(self) -> None:
        for _ in range(len(self.statements) * 2):
            if random() < 0.95:
                choice(self.statements).mutate()
            else:
                self.statements[randint(0, len(self.statements) - 1)] = \
                    ExecutionBlock.generate_random_body_element(self.meta)

    def crossover(self, other: ExecutionBlock) -> None:
        max_index: int = min(len(self.statements), len(other.statements))
        if max_index <= 1:
            raise ValueError(f'At least one of the offsprings is too short for crossover!')

        start_index: int = randint(1, max_index - 1)

        self.statements[start_index: max_index], other.statements[start_index: max_index] = \
            deepcopy(other.statements[start_index: max_index]), deepcopy(self.statements[start_index: max_index])

    def visit_commands(self, context: InterpreterContext) -> None:
        for statement in self.statements:
            statement.visit(context)

    def __str__(self) -> str:
        tabs: str = '\t' * (self.meta.depth + 1)
        statements_print = '\n'.join([f'{tabs}{statement}' for statement in self.statements])
        return f'{{\n{statements_print}\n{tabs[1:]}}}'

    def __len__(self) -> int:
        return sum([len(child) for child in self.statements])


@dataclass(slots=True)
class Assigment(Rule, RestrictedRandomize):
    name: VariableNameToken
    assigment_value: Expression

    @classmethod
    def from_random(cls, meta: Metadata) -> Assigment:
        value: Expression = Expression.from_random(Metadata(meta.variables_scope, 0))
        if random() < 0.5 and not meta.is_empty():
            name: VariableNameToken = VariableNameToken(meta.get_random_name())
        else:
            name: VariableNameToken = VariableNameToken.from_random()
            meta.variables_scope.add(name.value)

        return cls(meta, name, value)

    def mutate(self) -> None:
        if random() < 0.5:
            self.name = VariableNameToken(self.meta.get_random_name())
        else:
            self.assigment_value.mutate()

    def visit_commands(self, context: InterpreterContext) -> None:
        context[str(self.name)] = self.assigment_value.visit(context)

    def __str__(self) -> str:
        return f'{self.name} = {self.assigment_value};'

    def __len__(self) -> int:
        return len(self.assigment_value) + 1


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
        if random() < 0.3:
            self.condition = Condition.from_random(Metadata(self.meta.variables_scope, 0))
        else:
            self.body.mutate()

        if self.else_statement is not None and random() < 0.5:
            self.else_statement.mutate()
        elif self.else_statement is None and random() < 0.5:
            self.else_statement = ExecutionBlock.from_random(
                Metadata(deepcopy(self.meta.variables_scope), self.meta.depth + 1)
            )

    def visit_commands(self, context: InterpreterContext) -> None:
        if self.condition.visit(context):
            self.body.visit(context)
        elif self.else_statement is not None:
            self.else_statement.visit(context)

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
class LoopStatement(Rule, RestrictedRandomize):
    condition: Condition
    body: ExecutionBlock

    @classmethod
    def from_random(cls, meta: Metadata) -> LoopStatement:
        condition: Condition = Condition.from_random(Metadata(meta.variables_scope, 0))
        body: ExecutionBlock = ExecutionBlock.from_random(Metadata(deepcopy(meta.variables_scope), meta.depth + 1))

        return cls(meta, condition, body)

    def mutate(self) -> None:
        if random() < 0.3:
            self.condition = Condition.from_random(Metadata(self.meta.variables_scope, 0))
        else:
            self.body.mutate()

    def visit_commands(self, context: InterpreterContext) -> None:
        while self.condition.visit(context):
            self.body.visit(context)

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
    def from_random(cls) -> IOType:
        options: list = [
            cls.WRITE,
            cls.READ,
        ]

        return choice(options)

    @classmethod
    def get_opposite(cls, io_type: IOType) -> IOType:
        if io_type == cls.READ:
            return cls.WRITE

        return cls.READ


@dataclass(slots=True)
class IOStatement(Rule, RestrictedRandomize):
    io_type: IOType
    body: VariableNameToken | Expression

    @classmethod
    def from_random(cls, meta: Metadata) -> IOStatement:
        io_type: IOType = IOType.from_random()
        match io_type:
            case IOType.READ:
                if random() < 0.5 and not meta.is_empty():
                    body: VariableNameToken = VariableNameToken(meta.get_random_name())
                else:
                    body: VariableNameToken = VariableNameToken.from_random()
                    meta.variables_scope.add(body.value)

            case IOType.WRITE | _:
                body: Expression = Expression.from_random(Metadata(meta.variables_scope, 0))

        return cls(meta, io_type, body)

    def mutate(self) -> None:
        template: IOStatement = IOStatement.from_random(self.meta)
        self.io_type = template.io_type
        self.body = template.body

    def visit_commands(self, context: InterpreterContext) -> None:
        match self.io_type:
            case IOType.READ:
                context[str(self.body)] = context.mode.read()

            case IOType.WRITE:
                context.mode.write(self.body.visit(context))

    def __str__(self) -> str:
        return f'{self.io_type}({self.body});'

    def __len__(self) -> int:
        match self.io_type:
            case IOType.READ:
                return 2

            case IOType.WRITE | _:
                return len(self.body) + 1


@dataclass(slots=True)
class Condition(Rule, RestrictedRandomize):
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

                return [
                    BooleanToken
                ]

            case GenerationMethod.GROW:
                output: list = [
                    BooleanToken
                ]
                if meta.is_depth_in_limits():
                    output.extend([
                        (Expression, choice(('==', '!=', '>', '<', '>=', '<=')), Expression),
                        (Condition, choice(('&&', '||')), Condition),
                        Condition,
                    ])

                return output

    def mutate(self) -> None:
        match self.body:
            case (Expression() as left, _, Expression() as right):
                if random() < 0.5:
                    left.mutate()
                else:
                    right.mutate()
                self.body = (left, choice(('==', '!=', '>', '<', '>=', '<=')), right)

            case (Condition() as left, _, Condition() as right):
                if random() < 0.5:
                    left.mutate()
                else:
                    right.mutate()
                self.body = (left, choice(('&&', '||')), right)

            case Condition() as value:
                if random() < 0.5:
                    value.mutate()
                else:
                    self.body = self.body.body

            case BooleanToken() as value:
                self.body = value.from_random()

    def visit_commands(self, context: InterpreterContext) -> bool:
        match self.body:
            case (left, operation, right):
                left_value: bool | int = left.visit(context)
                right_value: bool | int = right.visit(context)

                match operation:
                    case '==':
                        return left_value == right_value

                    case '!=':
                        return left_value != right_value

                    case '>':
                        return left_value > right_value

                    case '<':
                        return left_value < right_value

                    case '>=':
                        return left_value >= right_value

                    case '<=':
                        return left_value <= right_value

                    case '&&':
                        return left_value and right_value

                    case '||':
                        return left_value or right_value

            case Condition() as option:
                return not option.visit(context)

            case _:
                return self.body.value

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
class Expression(Rule, RestrictedRandomize):
    body: ExpressionType

    @classmethod
    def from_random(cls, meta: Metadata) -> Expression:
        table_of_choices: list = cls.generate_choices(meta)

        match choice(table_of_choices):
            case (right, operation, left):
                deeper_meta: Metadata = Metadata(meta.variables_scope, meta.depth + 1)
                return cls(meta, (left.from_random(deeper_meta), operation, right.from_random(deeper_meta)))

            case self_namespace.VariableNameToken:
                return cls(meta, VariableNameToken(meta.get_random_name()))

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
                if not meta.is_empty():
                    output.extend([
                        VariableNameToken,
                    ])

                return output

            case GenerationMethod.GROW:
                output: list = [
                    IntegerToken,
                ]
                if not meta.is_empty():
                    output.extend([
                        VariableNameToken,
                    ])

                if meta.is_depth_in_limits():
                    output.extend([
                        (Expression, choice(('+', '-', '*', '/')), Expression),
                    ])

                return output

    def mutate(self) -> None:
        match self.body:
            case (Expression() as left, _, Expression() as right):
                if random() < 0.5:
                    left.mutate()
                else:
                    right.mutate()
                self.body = (left, choice(('+', '-', '*', '/')), right)

            case VariableNameToken():
                self.body = self.meta.get_random_name()

            case IntegerToken() as value:
                self.body = value.from_random()

    def visit_commands(self, context: InterpreterContext) -> int:
        match self.body:
            case (left, operation, right):
                left_value: int = left.visit(context)
                right_value: int = right.visit(context)

                match operation:
                    case '+':
                        return left_value + right_value

                    case '-':
                        return left_value - right_value

                    case '*':
                        return left_value * right_value

                    case '/':
                        if right_value == 0:
                            return left_value
                        return left_value // right_value

            case IntegerToken(value):
                return value

            case _ as option:
                variable_name: str = str(option)
                value: int = context[variable_name]

                if value is None:
                    context[variable_name] = context.mode.read()
                    return context[variable_name]

                return value

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


type ExpressionType = Tuple[Expression, str, Expression] | VariableNameToken | IntegerToken
type ConditionType = Tuple[Condition, str, Condition] | Tuple[Expression, str, Expression] | Condition \
                     | VariableNameToken | BooleanToken
type StatementBodyTypes = Assigment | IfStatement | LoopStatement | IOStatement

self_namespace = SimpleNamespace(**{
    cls.__name__: cls for _, cls in inspect.getmembers(
        importlib.import_module(__name__),
        inspect.isclass
    )
})
