from __future__ import annotations
from dataclasses import dataclass, field
from enum import Enum, auto
from random import random, choice
from typing import Union, Optional, List, Tuple

from src.genetic.individual.probability.subsequent_node_probability import SubsequentNodeProbability
from src.genetic.individual.structure.grammar_node import GrammarNode
from src.genetic.individual.tokens.tokens import VariableNameToken, IntegerToken, BooleanToken


@dataclass(slots=True, frozen=True)
class Program(GrammarNode):
    body: ExecutionBlock

    @classmethod
    def from_random(cls) -> Program:
        block: ExecutionBlock = ExecutionBlock.from_random()
        return cls(block)

    def mutate(self) -> Program:
        pass

    def crossover(self, other: Program) -> Program:
        pass

    def __str__(self) -> str:
        return str(self.body)


@dataclass(slots=True, frozen=True)
class ExecutionBlock(GrammarNode):
    statements: list[Statement] = field(default_factory=list)

    @classmethod
    def from_random(cls) -> ExecutionBlock:
        body: list[Statement] = []
        probability: SubsequentNodeProbability = SubsequentNodeProbability()

        while next(probability) > random():
            body.append(Statement.from_random())

        return cls(body)

    def mutate(self) -> ExecutionBlock:
        pass

    def crossover(self, other: ExecutionBlock) -> ExecutionBlock:
        pass

    def __str__(self) -> str:
        statements_print = '\n'.join([str(statement) for statement in self.statements])
        return f'{{\n{statements_print}\n}}\n'


@dataclass(slots=True, frozen=True)
class Statement(GrammarNode):
    body: StatementBodyTypes

    @classmethod
    def from_random(cls) -> Statement:
        statement_constructor = choice([VarDeclaration, Assigment, IfStatement, LoopStatement, IOStatement])
        body: StatementBodyTypes = statement_constructor.from_random()
        return cls(body)

    def mutate(self) -> Statement:
        pass

    def crossover(self, other: Statement) -> Statement:
        pass

    def __str__(self):
        return str(self.body)


@dataclass(slots=True, frozen=True)
class VarDeclaration(GrammarNode):
    is_constant: bool
    declaration: DeclarationTypes

    @classmethod
    def from_random(cls) -> VarDeclaration:
        is_constant = choice([True, False])
        declaration: DeclarationTypes = choice([IntegerDeclaration, BooleanDeclaration]).from_random()

        return cls(is_constant, declaration)

    def mutate(self) -> VarDeclaration:
        pass

    def crossover(self, other: VarDeclaration) -> VarDeclaration:
        pass

    def __str__(self):
        return f'{"const " if self.is_constant else ""}{self.declaration};'


@dataclass(slots=True, frozen=True)
class Assigment(GrammarNode):
    name: VariableNameToken
    assigment_value: AssigmentValueType

    @classmethod
    def from_random(cls) -> Assigment:
        name: VariableNameToken = VariableNameToken.from_random()
        value: AssigmentValueType = choice([Expression, Condition]).from_random()  # Don't forget Validation...

        return cls(name, value)

    def mutate(self) -> Assigment:
        pass

    def crossover(self, other: Assigment) -> Assigment:
        pass

    def __str__(self):
        return f'{self.name} = {self.assigment_value}'


@dataclass(slots=True, frozen=True)
class IfStatement(GrammarNode):
    condition: Condition
    body: ExecutionBlock
    else_statement: Optional[ExecutionBlock]

    @classmethod
    def from_random(cls) -> IfStatement:
        condition: Condition = Condition.from_random()
        body: ExecutionBlock = ExecutionBlock.from_random()

        else_constructor = choice([ExecutionBlock, None])
        if else_constructor is not None:
            else_statement: Optional[ExecutionBlock] = ExecutionBlock.from_random()
        else:
            else_statement = None

        return cls(condition, body, else_statement)

    def mutate(self) -> IfStatement:
        pass

    def crossover(self, other: IfStatement) -> IfStatement:
        pass

    def __str__(self):
        base: str = f'if ({self.condition}) {self.body}'

        if self.else_statement is not None:
            return base + f' else {self.else_statement}'

        return base


@dataclass(slots=True, frozen=True)
class LoopStatement(GrammarNode):
    condition: Condition
    body: ExecutionBlock

    @classmethod
    def from_random(cls) -> LoopStatement:
        condition: Condition = Condition.from_random()
        body: ExecutionBlock = ExecutionBlock.from_random()

        return cls(condition, body)

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
class IOStatement(GrammarNode):
    io_type: IOType
    name: VariableNameToken

    @classmethod
    def from_random(cls) -> IOStatement:
        io_type: IOType = IOType.from_random()
        name: VariableNameToken = VariableNameToken.from_random()
        return cls(io_type, name)

    def mutate(self) -> IOStatement:
        pass

    def crossover(self, other: IOStatement) -> IOStatement:
        pass

    def __str__(self):
        return f'{self.io_type} ({self.name});'


@dataclass(slots=True, frozen=True)
class IntegerDeclaration(GrammarNode):
    name: VariableNameToken
    expression: Optional[Expression]

    @classmethod
    def from_random(cls) -> IntegerDeclaration:
        name: VariableNameToken = VariableNameToken.from_random()

        expression_constructor = choice([Expression, None])
        if expression_constructor is not None:
            expression = expression_constructor.from_random()
        else:
            expression = None

        return cls(name, expression)

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
class BooleanDeclaration(GrammarNode):
    name: VariableNameToken
    condition: Optional[Condition]

    @classmethod
    def from_random(cls) -> BooleanDeclaration:
        name: VariableNameToken = VariableNameToken.from_random()

        condition_constructor = choice([Condition, None])
        if condition_constructor is not None:
            condition = condition_constructor.from_random()
        else:
            condition = None

        return cls(name, condition)

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
class Condition(GrammarNode):
    body: ConditionType

    @classmethod
    def from_random(cls) -> Condition:
        table_of_choices: List = [
            (Expression, choice(['==', '!=', '>', '<', '>=', '<=']), Expression),
            (Condition, choice(['&&', '||', '^']), Condition),
            Condition,
            VariableNameToken,
            BooleanToken,
        ]

        match choice(table_of_choices):
            case (right, operation, left):
                return cls((left.from_random(), operation, right.from_random()))

            case _ as option:
                return cls(option.from_random())

    def mutate(self) -> Condition:
        pass

    def crossover(self, other: Condition) -> Condition:
        pass

    def __str__(self):
        match self.body:
            case (left, operation, right):
                return f'{left} {operation} {right}'

            case Condition(_) as value:
                return f'!({str(value)})'

            case _ as value:
                return str(value)


@dataclass(slots=True, frozen=True)
class Expression(GrammarNode):
    body: ExpressionType

    @classmethod
    def from_random(cls) -> Expression:
        table_of_choices: List = [
            (Expression, choice(['+', '-', '*', '/']), Expression),
            VariableNameToken,
            IntegerToken,
        ]

        match choice(table_of_choices):
            case (right, operation, left):
                return cls((left.from_random(), operation, right.from_random()))

            case _ as option:
                return cls(option.from_random())

    def mutate(self) -> Expression:
        pass

    def crossover(self, other: Expression) -> Expression:
        pass

    def __str__(self):
        match self.body:
            case (Expression(_) as left, operation, Expression(_) as right):
                return f'{left} {operation} {right}'

            case _ as value:
                return str(value)


ExpressionType = Union[Tuple[Expression, str, Expression], VariableNameToken, IntegerToken]
ConditionType = Union[Tuple[Condition, str, Condition], Tuple[Expression, str, Expression], Condition, VariableNameToken, BooleanToken]
StatementBodyTypes = Union[VarDeclaration, Assigment, IfStatement, LoopStatement, IOStatement]
DeclarationTypes = Union[IntegerDeclaration, BooleanDeclaration]
AssigmentValueType = Union[Expression, Condition]
