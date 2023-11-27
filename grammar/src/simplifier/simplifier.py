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
        for index in range(len(self.program)):
            pass

        return self.program.count('(') - self.simplify().count('(')


    def locate_simplifiable(self) -> int:
        pass

    @staticmethod
    def locate_parentheses(input_sequence: str) -> Optional[Tuple[int, int]]:
        opening_parenthesis_index: int = input_sequence.find('(')
        closing_parenthesis_index: int = input_sequence.rfind(')')

        if opening_parenthesis_index == -1 or closing_parenthesis_index == -1:
            return None

        return opening_parenthesis_index, closing_parenthesis_index

    def is_satisfiable(self, opening_parenthesis_index: int, closing_parenthesis_index: int) -> bool:
        sub_formula: str = self.program[opening_parenthesis_index: closing_parenthesis_index]

        return 'X' in sub_formula or \
               self.program[opening_parenthesis_index] == '(' or \
               self.program[closing_parenthesis_index] == ')'