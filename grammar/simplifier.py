from typing import Tuple, Union, Any, Optional, Literal
from re import compile
from sys import argv

from src.tiny_gp.operator_logic import OperatorLogic


class Simplifier:
    _tokenizer = compile(r'([()])|\s+').split

    def __init__(self, input_formula: str):
        self.output: str = input_formula[1: -1]

    def simplify(self) -> str:
        out = self.parse_conditions()
        return str(Simplifier.calculate(out))

    @staticmethod
    def tokenize(s) -> map:
        def _helper(val: str) -> Union[float, str]:
            try:
                return float(val)
            except ValueError:
                return val

        return map(_helper, filter(None, Simplifier._tokenizer(s)))

    def parse_conditions(self) -> list:
        def _helper(tokens) -> Tuple[list, bool]:
            items = []
            for item in tokens:
                match item:
                    case '(':
                        result, close_parentheses_status = _helper(tokens)
                        if close_parentheses_status:
                            raise ValueError(f'Unbalanced parentheses found in expression: \"{self.output}\".')

                        items.append(result)

                    case ')':
                        return items, False

                    case _:
                        items.append(item)

            return items, True

        return _helper(Simplifier.tokenize(self.output))[0]

    @staticmethod
    def correct_chaining_standard(un_simplifiable: Union[list, str], left_operation: str, right_operation: str, first_val: float, second_val: float) -> Optional[list]:
        match (left_operation, right_operation):
            case ('+', '+'):
                return [un_simplifiable, '+', OperatorLogic.add(first_val, second_val)]

            case ('+', '-'):
                result: float = OperatorLogic.sub(first_val, second_val)
                return [un_simplifiable, '+' if result >= 0.0 else '-', abs(result)]

            case ('-', '+'):
                result: float = OperatorLogic.add(-first_val, second_val)
                return [un_simplifiable, '+' if result >= 0.0 else '-', abs(result)]

            case ('-', '-'):
                return [un_simplifiable, '-', OperatorLogic.add(first_val, second_val)]

            case ('*', '*'):
                return [un_simplifiable, '*', OperatorLogic.multiply(first_val, second_val)]

            case ('*', '/'):
                return [un_simplifiable, '*', OperatorLogic.multiply(first_val, OperatorLogic.divide(1.0, second_val))]

            case ('/', '*'):
                return [un_simplifiable, '*', OperatorLogic.multiply(OperatorLogic.divide(1.0, first_val), second_val)]

            case ('/', '/'):
                return [un_simplifiable, '/', OperatorLogic.multiply(first_val, second_val)]

            case _:
                return None

    @staticmethod
    def calculate(expression: list) -> Union[float, list]:
        match expression:

            case [str(left), ('+' | '-' | '*' | '/'), str(right)] as option if 'X' in left and 'X' in right:
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

                output: list[Any] = [left_out, operation, right_out]

                if isinstance(left_out, list) and isinstance(right_out, list):
                    return output

                if isinstance(left_out, list) and not isinstance(right_out, list):

                    match output:
                        case [[left_left_val, left_operation, float(left_right_val)], right_operation, float(right_val)] if isinstance(left_left_val, list) or 'X' in left_left_val:
                            chain_output: Optional[list] = Simplifier.correct_chaining_standard(left_left_val, left_operation, right_operation, left_right_val, right_val)
                            if chain_output is None:
                                return output

                            return chain_output

                        case [[float(left_left_val), left_operation, left_right_val], right_operation, float(right_val)] if isinstance(left_right_val, list) or 'X' in left_right_val:
                            chain_output: Optional[list] = Simplifier.correct_chaining_standard(left_right_val, left_operation, right_operation, left_left_val, right_val)[::-1]
                            if chain_output is None:
                                return output

                            return chain_output

                        case _:
                            return output

                if not isinstance(left_out, list) and isinstance(right_out, list):

                    match output:
                        case [float(left_val), left_operation, [float(left_right_val), right_operation, right_right_val]] if isinstance(right_right_val, list) or 'X' in right_right_val:
                            chain_output: Optional[list] = Simplifier.correct_chaining_standard(right_right_val, left_operation, right_operation, left_val, left_right_val)[::-1]
                            if chain_output is None:
                                return output

                            return chain_output

                        case [float(left_val), left_operation, [left_right_val, right_operation, float(right_right_val)]] if isinstance(left_right_val, list) or 'X' in left_right_val:
                            chain_output: Optional[list] = Simplifier.correct_chaining_standard(left_right_val, left_operation, right_operation, left_val, right_right_val)
                            if chain_output is None:
                                return output

                            return chain_output

                        case _:
                            return output

                return Simplifier.calculate([left_out, operation, right_out])

            case [list(left), ('+' | '-' | '*' | '/') as operation, float(right)]:
                left_out: Union[float, list] = Simplifier.calculate(left)

                if isinstance(left_out, list):
                    output: list[Any] = [left_out, operation, right]

                    match output:
                        case [[left_left_val, left_operation, float(left_right_val)], right_operation, float(right_val)] if isinstance(left_left_val, list) or 'X' in left_left_val:
                            chain_output: Optional[list] = Simplifier.correct_chaining_standard(left_left_val, left_operation, right_operation, left_right_val, right_val)
                            if chain_output is None:
                                return output

                            return chain_output

                        case [[float(left_left_val), left_operation, left_right_val], right_operation, float(right_val)] if isinstance(left_right_val, list) or 'X' in left_right_val:
                            chain_output: Optional[list] = Simplifier.correct_chaining_standard(left_right_val, left_operation, right_operation, left_left_val, right_val)[::-1]
                            if chain_output is None:
                                return output

                            return chain_output

                        case _:
                            return output

                return Simplifier.calculate([left_out, operation, right])

            case [float(left), ('+' | '-' | '*' | '/') as operation, list(right)]:
                right_out: Union[float, list] = Simplifier.calculate(right)

                if isinstance(right_out, list):
                    output: list[Any] = [left, operation, right_out]

                    match output:
                        case [float(left_val), left_operation, [float(left_right_val), right_operation, right_right_val]] if isinstance(right_right_val, list) or 'X' in right_right_val:
                            chain_output: Optional[list] = Simplifier.correct_chaining_standard(right_right_val, left_operation, right_operation, left_val, left_right_val)[::-1]
                            if chain_output is None:
                                return output

                            return chain_output

                        case [float(left_val), left_operation, [left_right_val, right_operation, float(right_right_val)]] if isinstance(left_right_val, list) or 'X' in left_right_val:
                            chain_output: Optional[list] = Simplifier.correct_chaining_standard(left_right_val, left_operation, right_operation, left_val, right_right_val)
                            if chain_output is None:
                                return output

                            return chain_output

                        case _:
                            return output

                return Simplifier.calculate([left, operation, right_out])

            case [left, '+', right]:
                return OperatorLogic.add(left, right)

            case [left, '-', right]:
                return OperatorLogic.sub(left, right)

            case [left, '*', right]:
                return OperatorLogic.multiply(left, right)

            case [left, '/', right]:
                return OperatorLogic.divide(left, right)

            case ['sin', list(val)]:
                val: Union[float, list] = Simplifier.calculate(val)

                if isinstance(val, list):
                    return ['sin', val]

                return OperatorLogic.sin(val)

            case ['cos', list(val)]:
                val: Union[float, list] = Simplifier.calculate(val)

                if isinstance(val, list):
                    return ['cos', val]

                return OperatorLogic.cos(val)

            case [str(val)] if 'X' in val:
                return [val]

            case [list(val)]:
                return Simplifier.calculate(val)

            case [float(val)]:
                return val

            case _:
                raise ValueError(f'Invalid expression: \"{expression}\". No rule was found.')


class ExpressionSimplifier:
    pass


def cut_program_from_file(file_path: str) -> str:
    with open(file_path, 'r') as input_file:
        raw_input = input_file.readlines()

        return raw_input[-2].lstrip("Best Individual: ")


def main() -> None:
    program: str = cut_program_from_file(argv[1])
    simplifier: Simplifier = Simplifier(program)

    # simplifier: Simplifier = Simplifier("((1 * (3.2 + 3.4)) * 3)")
    # print(simplifier.simplify())

    # simplifier: Simplifier = Simplifier('(((cos((sin((0.15792111801538056 / ((sin((((cos(4.390922989460659)) - (cos((sin(((3.9378125013554417 - (4.567186184882816 + (4.9798113857157915 - (2.879804272999489 + 1.8159963035888813)))) * 1.636289987009465)))))) - 4.167758199134466))) - 2.0531718571910895)))))) / 2.637638162486309) + (1.6247319950636392 + (X1 * X1)))')
    # print(simplifier.simplify())

    # simplifier: Simplifier = Simplifier('(0.3752679242505537 + (1.6247319950636392 + (X1 * X1)))')
    # print(simplifier.simplify())

    # simplifier: Simplifier = Simplifier("(1 * ((( 3.2 + 3.4) / ( 3.3 + 3.3)) * 2))")
    # print(simplifier.simplify())

    # simplifier: Simplifier = Simplifier("(((sin(1)) + 1))")
    # print(simplifier.simplify())

    # simplifier: Simplifier = Simplifier("(((sin(1)) + X1))")
    # print(simplifier.simplify())

    # simplifier: Simplifier = Simplifier("((X1 * ( 3.2 + 3.4)) * 2)")
    # print(simplifier.simplify())

    # simplifier: Simplifier = Simplifier("((( 3.2 + 3.4) * X1) * 2)")
    # print(simplifier.simplify())

    # simplifier: Simplifier = Simplifier("((( 3.2 + 3.4) + X1) + 2)")
    # print(simplifier.simplify())

    # simplifier: Simplifier = Simplifier("(2 + (( 3.2 + 3.4) + X1))")
    # print(simplifier.simplify())

    # simplifier: Simplifier = Simplifier("(2 + (X1 + ( 3.2 + 3.4)))")
    # print(simplifier.simplify())

    # simplifier: Simplifier = Simplifier("(X1  * ((( 3.2 + 3.4) / ( 3.3 + 3.3)) * 2))")
    # print(simplifier.simplify())

    with open(argv[2], 'w') as output_file:
        output_file.write(simplifier.simplify())


if __name__ == '__main__':
    main()
