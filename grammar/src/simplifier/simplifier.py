from math import sin, cos
from sys import argv
from typing import Optional, Tuple


class Simplifier:

    def __init__(self, program: str):
        self.program: str = program
        self.output: str = self.program.lstrip('(').rstrip(')')

    def simplify(self) -> str:
        formulas_count: int = self.count_simplifiable()

        while True:


            if  formulas_count == 0:
                break

        return f'({self.output})'

    def count_simplifiable(self) -> int:
        pass

    def locate_simplifiable(self) -> int:
        pass

    def locate_formulas(self) -> Tuple[int, int]:
        count: int = 0

    def is_satisfiable(self, opening_parenthesis_index: int, closing_parenthesis_index: int) -> bool:
        """
        Checks if the sub-formula is satisfiable.

        :param opening_parenthesis_index:
        :param closing_parenthesis_index:
        :return:
        """
        if self.program[opening_parenthesis_index] == '(':
            raise ValueError('Invalid opening parenthesis index')

        if self.program[closing_parenthesis_index] == ')':
            raise ValueError('Invalid closing parenthesis index')

        sub_formula: str = self.program[opening_parenthesis_index: closing_parenthesis_index]

        return 'X' in sub_formula

    @staticmethod
    def locate_parentheses(input_sequence: str) -> Tuple[Optional[int], Optional[int]]:
        opening_parenthesis_index: int = input_sequence.find('(')
        closing_parenthesis_index: int = input_sequence.find(')')

        opening_parenthesis_index = None if opening_parenthesis_index == -1 else opening_parenthesis_index
        closing_parenthesis_index = None if closing_parenthesis_index == -1 else closing_parenthesis_index

        return opening_parenthesis_index, closing_parenthesis_index

    def split_to_tokens(self, sub_formula: str) -> Tuple[str, float, Optional[float]]:
        tokens: list[str] = sub_formula.split()



    @staticmethod
    def calculate_result(function: str, left_element: float, right_element: Optional[float] = None) -> float:
        match function:
            case "+":
                return left_element + right_element
            case "-":
                return left_element - right_element
            case "*":
                return left_element * right_element
            case "/":
                return left_element / right_element if abs(right_element) <= 0.001 else right_element
            case "sin":
                return sin(left_element)
            case "cos":
                return cos(left_element)
            case _:
                raise ValueError(f'Invalid function: {function}')

    def replace_sub_formula(self, sub_formula: str):
        pass


def cut_program_from_file(file_path: str) -> str:
    with open(file_path, 'r') as input_file:
        raw_input = input_file.read()

        lines = raw_input.split('\n')

        return lines[len(lines) - 2].lstrip("Best Individual: ")


if __name__ == '__main__':
    program: str = cut_program_from_file(argv[1])
    simplifier = Simplifier(program)
    with open(argv[2], 'w') as output_file:
        output_file.write(simplifier.simplify())
