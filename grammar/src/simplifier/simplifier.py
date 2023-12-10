from typing import Optional, Tuple, Union, Callable
from math import sin, cos
from sys import argv
import re


class Simplifier:
    _tokenizer = re.compile(r'([()])|\s+').split

    def __init__(self, input_formula: str):
        self.output: str = input_formula[1: -1]

    def simplify(self) -> str:
        out = Simplifier.parse_conditions(self.output)
        print(out)
        return f'({Simplifier.calculate(out)})'

    @staticmethod
    def tokenize(s):
        def _helper(val: str) -> Union[float, str]:
            try:
                return float(val)
            except ValueError:
                return val

        return map(_helper, filter(None, Simplifier._tokenizer(s)))

    @staticmethod
    def parse_conditions(expr) -> list:
        def _helper(tokens) -> Tuple[list, bool]:
            items = []
            for item in tokens:
                if item == '(':
                    result, closeparen = _helper(tokens)
                    if not closeparen:
                        raise ValueError("Unbalanced parentheses")
                    items.append(result)
                elif item == ')':
                    return items, True
                else:
                    items.append(item)
            return items, False

        return _helper(Simplifier.tokenize(expr))[0]

    @staticmethod
    def calculate(expression: list) -> Optional[float]:
        match expression:

            case [left, operation, right] if isinstance(left, list) and isinstance(right, list):
                left_out: float = Simplifier.calculate(left)
                right_out: float = Simplifier.calculate(right)
                return Simplifier.calculate([left_out, operation, right_out])

            case [left, operation, right] if isinstance(left, list):
                left_out = Simplifier.calculate(left)
                return Simplifier.calculate([left_out, operation, right])

            case [left, operation, right] if isinstance(right, list):
                right_out = Simplifier.calculate(right)
                return Simplifier.calculate([left, operation, right_out])

            case [left, '+', right]:
                return left + right

            case [left, '-', right]:
                return left - right

            case [left, '*', right]:
                return left * right

            case [left, '/', right]:
                return left / right if abs(right) <= 0.001 else right

            case ['sin', val]:
                val: float = Simplifier.calculate(val)
                return sin(val)

            case ['cos', val]:
                val: float = Simplifier.calculate(val)
                return cos(val)

            case [val] if isinstance(val, list):
                return Simplifier.calculate(val)

            case [val] if isinstance(val, float):
                return val

            case _:
                raise ValueError(f'Invalid expression: {expression}')


def cut_program_from_file(file_path: str) -> str:
    with open(file_path, 'r') as input_file:
        raw_input = input_file.read()

        lines = raw_input.split('\n')

        return lines[len(lines) - 3].lstrip("Best Individual: ")


if __name__ == '__main__':
    # print("((cos(1)) + 1)")

    # program: str = cut_program_from_file(argv[1])
    # simplifier: Simplifier = Simplifier(program)
    simplifier: Simplifier = Simplifier("((1 * (3.2 + 3.4)) * 3)")
    print(simplifier.simplify())

    simplifier: Simplifier = Simplifier("(1 * ((( 3.2 + 3.4) / ( 3.3 + 3.3)) * 2))")
    print(simplifier.simplify())

    simplifier: Simplifier = Simplifier("(((sin(1)) + 1))")
    print(simplifier.simplify())

# with open(argv[2], 'w') as output_file:
#     output_file.write(simplifier.simplify())
