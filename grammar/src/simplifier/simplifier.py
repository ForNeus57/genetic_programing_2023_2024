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
        return f'({Simplifier.calculate(out)})\n'

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
    def calculate(expression: list) -> Union[float, list]:
        match expression:

            case [str(left), _, str(right)] as option if 'X' in left and 'X' in right:
                return option

            case [str(left), ('+' | '-' | '*' | '/') as operation, right] if 'X' in left:
                if isinstance(right, list):
                    right: Union[list, float] = Simplifier.calculate(right)

                return [left, operation, right]

            case [left, ('+' | '-' | '*' | '/') as operation, str(right)] if 'X' in right:
                if isinstance(left, list):
                    left: Union[list, float] = Simplifier.calculate(left)

                return [left, operation, right]

            case [list(left), ('+' | '-' | '*' | '/') as operation, list(right)]:
                left_out: Union[float, list] = Simplifier.calculate(left)
                right_out: Union[float, list] = Simplifier.calculate(right)

                if isinstance(left_out, list) or isinstance(right_out, list):
                    return [left_out, operation, right_out]

                return Simplifier.calculate([left_out, operation, right_out])

            case [list(left), ('+' | '-' | '*' | '/') as operation, right]:
                left_out: Union[float, list] = Simplifier.calculate(left)

                if isinstance(left_out, list):
                    return [left_out, operation, right]

                return Simplifier.calculate([left_out, operation, right])

            case [left, ('+' | '-' | '*' | '/') as operation, list(right)]:
                right_out: Union[float, list] = Simplifier.calculate(right)

                if isinstance(right_out, list):
                    return [right_out, operation, right]

                return Simplifier.calculate([left, operation, right_out])

            case [left, '+', right]:
                return left + right

            case [left, '-', right]:
                return left - right

            case [left, '*', right]:
                return left * right

            case [left, '/', right]:
                return left / right if abs(right) > 0.001 else right

            case ['sin', val]:
                val: Union[float, list] = Simplifier.calculate(val)

                if isinstance(val, list):
                    return ['sin', val]

                return sin(val)

            case ['cos', val]:
                val: Union[float, list] = Simplifier.calculate(val)

                if isinstance(val, list):
                    return ['cos', val]

                return cos(val)

            case [list(val)]:
                return Simplifier.calculate(val)

            case [float(val)]:
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

    simplifier: Simplifier = Simplifier("(((sin(1)) + X1))")
    print(simplifier.simplify())

    simplifier: Simplifier = Simplifier("((X1  * ( 3.2 + 3.4)) * 2)")
    print(simplifier.simplify())

    simplifier: Simplifier = Simplifier("(X1  * ((( 3.2 + 3.4) / ( 3.3 + 3.3)) * 2))")
    print(simplifier.simplify())

# with open(argv[2], 'w') as output_file:
#     output_file.write(simplifier.simplify())
