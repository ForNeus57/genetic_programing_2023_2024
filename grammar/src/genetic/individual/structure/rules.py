from __future__ import annotations
from dataclasses import dataclass, field
from typing import Union, Optional, List, Tuple
from random import random, choice, randint
from enum import Enum, auto

from src.genetic.individual.interfaces.node_types import Rule
from src.genetic.individual.probability.exponential_probability import ExponentialProbability
from src.genetic.individual.interfaces.randomize import Randomize, RestrictedRandomize
from src.genetic.individual.structure.tokens import VariableNameToken, IntegerToken, BooleanToken


@dataclass(slots=True, frozen=True)
class Program(Rule, Randomize):
    body: ExecutionBlock

    @classmethod
    def from_random(cls) -> Program:
        block: ExecutionBlock = ExecutionBlock.from_random(1)
        return cls(0, block)

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
    def from_random(cls, depth: int) -> ExecutionBlock:
        body: list[Statement] = []
        probability: ExponentialProbability = ExponentialProbability()

        while next(probability) > random():
            body.append(Statement.from_random(depth))

        return cls(depth, body)

    def mutate(self) -> ExecutionBlock:
        pass

    def crossover(self, other: ExecutionBlock) -> ExecutionBlock:
        pass

    def __str__(self) -> str:
        tabs: str = '\t' * self.depth
        statements_print = '\n'.join([f'{tabs}{statement}' for statement in self.statements])
        return f'{{\n{statements_print}\n{tabs[2:]}}}\n'


@dataclass(slots=True, frozen=True)
class Statement(Rule, RestrictedRandomize):
    body: StatementBodyTypes

    @classmethod
    def from_random(cls, depth: int) -> Statement:
        if depth > cls.max_depth:
            statement_constructor_table = [VarDeclaration, Assigment, IOStatement]
        else:
            statement_constructor_table = [VarDeclaration, Assigment, IfStatement, LoopStatement, IOStatement]

        chosen_index: int = randint(0, len(statement_constructor_table) - 1)

        statement_constructor = statement_constructor_table[chosen_index]
        match chosen_index:
            case 2 | 3:
                body: StatementBodyTypes = statement_constructor.from_random(depth + 1)

            case _:
                body: StatementBodyTypes = statement_constructor.from_random(depth)

        return cls(depth, body)

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
    def from_random(cls, depth: int) -> VarDeclaration:
        is_constant = choice([True, False])
        declaration: DeclarationTypes = choice([IntegerDeclaration, BooleanDeclaration]).from_random(depth + 1)

        return cls(depth, is_constant, declaration)

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
    def from_random(cls, depth: int) -> Assigment:
        name: VariableNameToken = VariableNameToken.from_random()
        value: AssigmentValueType = choice([Expression, Condition]).from_random(depth + 1)  # Don't forget Validation...

        return cls(depth, name, value)

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
    def from_random(cls, depth: int) -> IfStatement:
        condition: Condition = Condition.from_random(depth + 1)
        body: ExecutionBlock = ExecutionBlock.from_random(depth + 1)

        else_constructor = choice([ExecutionBlock, None])
        if else_constructor is not None:
            else_statement: ExecutionBlock = ExecutionBlock.from_random(depth + 1)
        else:
            else_statement: Optional[ExecutionBlock] = None

        return cls(depth, condition, body, else_statement)

    def mutate(self) -> IfStatement:
        pass

    def crossover(self, other: IfStatement) -> IfStatement:
        pass

    def __str__(self):
        base: str = f'if ({self.condition}) {self.body}'

        if self.else_statement is not None:
            indentation: str = '\t' * (self.depth - 1)
            return base + f'{indentation} else {self.else_statement}'

        return base


@dataclass(slots=True, frozen=True)
class LoopStatement(Rule, RestrictedRandomize):
    condition: Condition
    body: ExecutionBlock

    @classmethod
    def from_random(cls, depth: int) -> LoopStatement:
        condition: Condition = Condition.from_random(depth + 1)
        body: ExecutionBlock = ExecutionBlock.from_random(depth + 1)

        return cls(depth, condition, body)

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
    def from_random(cls, depth: int) -> IOStatement:
        io_type: IOType = IOType.from_random()
        name: VariableNameToken = VariableNameToken.from_random()
        return cls(depth, io_type, name)

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
    def from_random(cls, depth: int) -> IntegerDeclaration:
        name: VariableNameToken = VariableNameToken.from_random()

        expression_constructor = choice([Expression, None])
        if expression_constructor is not None:
            expression = expression_constructor.from_random(depth + 1)
        else:
            expression = None

        return cls(depth, name, expression)

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
    def from_random(cls, depth: int) -> BooleanDeclaration:
        name: VariableNameToken = VariableNameToken.from_random()

        condition_constructor = choice([Condition, None])
        if condition_constructor is not None:
            condition = condition_constructor.from_random(depth + 1)
        else:
            condition = None

        return cls(depth, name, condition)

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
    def from_random(cls, depth: int) -> Condition:
        table_of_choices: List = [
            (Expression, choice(['==', '!=', '>', '<', '>=', '<=']), Expression),
            (Condition, choice(['&&', '||', '^']), Condition),
            Condition,
            VariableNameToken,
            BooleanToken,
        ]

        random_constructor_index = randint(0, len(table_of_choices) - 1)

        match random_constructor_index:
            case 0 | 1:
                left, operation, right = table_of_choices[random_constructor_index]
                return cls(depth, (left.from_random(depth + 1), operation, right.from_random(depth + 1)))

            case 2:
                option = table_of_choices[random_constructor_index]
                return cls(depth, option.from_random(depth + 1))

            case 3 | 4:
                option = table_of_choices[random_constructor_index]
                return cls(depth, option.from_random())

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
    def from_random(cls, depth: int) -> Expression:
        table_of_choices: List = [
            (Expression, choice(['+', '-', '*', '/']), Expression),
            VariableNameToken,
            IntegerToken,
        ]

        match choice(table_of_choices):
            case (right, operation, left):
                return cls(depth, (left.from_random(depth + 1), operation, right.from_random(depth + 1)))

            case _ as option:
                return cls(depth, option.from_random())

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
ConditionType = Union[Tuple[Condition, str, Condition], Tuple[Expression, str, Expression], Condition, VariableNameToken, BooleanToken]
StatementBodyTypes = Union[VarDeclaration, Assigment, IfStatement, LoopStatement, IOStatement]
DeclarationTypes = Union[IntegerDeclaration, BooleanDeclaration]
AssigmentValueType = Union[Expression, Condition]
