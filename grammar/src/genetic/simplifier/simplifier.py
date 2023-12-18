"""
.. module:: genetic.simplifier.simplifier
   :synopsis: A module for simplifying TinyGP expressions.

.. moduleauthor:: Dominik Breksa, dominikbreksa@gmail.com
"""

from typing import Tuple, Union, Any, Optional
from re import compile

from genetic.simplifier.tiny_gp.operator_logic import OperatorLogic


class Simplifier:
    """
    A class used to simplify TinyGP expressions.

    Attributes
    ----------
    input : str
        the output formula to be simplified
    tokens : map
        the tokenized output formula

    Methods
    -------
    simplify():
        Simplifies the output formula.
    _tokenize():
        Tokenizes the output formula.
    _parse_input():
        Parses the parenthesis in the tokenized formula.
    _double_simplify(un_simplifiable, left_operation, right_operation, first_val, second_val):
        Corrects the chaining standard of the formula.
    _calculate(expression):
        Calculates the value of the expression.
    """
    _tokenizer = compile(r'([()])|\s+').split

    def __init__(self, input_formula: str):
        """
        Constructs all the necessary attributes for the Simplifier object.

        Parameters
        ----------
            input_formula : str
                the input formula to be simplified
        """
        self.input: str = input_formula[1: -1]
        self.tokens: map = self._tokenize()

    def simplify(self) -> str:
        """
        Simplifies the output formula.

        Returns
        -------
        str
            the simplified formula
        """
        out = self._parse_input()
        return str(Simplifier._calculate(out))

    def _tokenize(self) -> map:
        """
        Tokenizes the output formula. Firstly it splits the formula by parentheses and then by whitespaces.
        Spaces on its own are not sufficient because it will not split for example '(abc' into ['(', 'abc'].
        It also filters out empty strings. And finally it converts all numbers to floats.

        Returns
        -------
        map
            the tokenized formula in from of iterable map
        """
        def _helper(val: str) -> Union[float, str]:
            try:
                return float(val)
            except ValueError:
                return val

        return map(_helper, filter(None, Simplifier._tokenizer(self.input)))

    def _parse_input(self) -> list:
        """
        Parses the conditions in the tokenized formula. In this context parsing means to split into sub lists
        by parentheses. For example from: ((1.2 + 1.3) * 0.2) -> [[1.2, '+', 1.3], '*', 0.2]. Utilizes iterator so that
        keeping track of index in input is not necessary.

        This method also checks for valid parentheses in the formula. If the parentheses are not balanced,
        it throws a ValueError.

        Returns
        -------
        list
            nested list of tokenized formula

        Raises
        ------
        ValueError
            If the parentheses in the formula are not balanced.
        """
        def _helper(tokens) -> Tuple[list, bool]:
            items = []
            for item in tokens:
                match item:
                    case '(':
                        result, close_parentheses_status = _helper(tokens)
                        if close_parentheses_status:
                            raise ValueError(f'Unbalanced parentheses found in expression: \"{self.input}\".')

                        items.append(result)

                    case ')':
                        return items, False

                    case _:
                        items.append(item)

            return items, True

        return _helper(self.tokens)[0]

    @staticmethod
    def _double_simplify(un_simplifiable: Union[list, str], left_operation: str, right_operation: str, first_val: float, second_val: float) -> Optional[list]:
        """
        Method that is used for example in this case:
        [['X', '+', 0.2], '+', 1.0] -> ['X', '+', 1.2]

        Notice that it can only be done in cases listed below. Otherwise, it returns None.

        Parameters
        ----------
        un_simplifiable : Union[list, str]
            the unsimplified part of the formula
        left_operation : str
            the left operation in the formula
        right_operation : str
            the right operation in the formula
        first_val : float
            the first value in the formula
        second_val : float
            the second value in the formula

        Returns
        -------
        Optional[list]
            returns the simplified formula if it is possible, otherwise returns None
        """
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
    def _calculate(expression: list) -> Union[float, list]:
        """
        It is the engine of simplification process. It recursively tries to simplify it via pattern matching. Each case
        is some type of rule, which is used to simplify the expression.

        Parameters
        ----------
        expression : list
            the expression to be calculated

        Returns
        -------
        Union[float, list]
            returns float if simplification was successful, otherwise returns list of unsimplified expression
        """
        match expression:

            case [str(left), ('+' | '-' | '*' | '/'), str(right)] as option if 'X' in left and 'X' in right:
                return option

            case [str(left), ('+' | '-' | '*' | '/') as operation, right] if 'X' in left:
                if isinstance(right, list):
                    right: Union[list, float] = Simplifier._calculate(right)

                return [left, operation, right]

            case [left, ('+' | '-' | '*' | '/') as operation, str(right)] if 'X' in right:
                if isinstance(left, list):
                    left: Union[list, float] = Simplifier._calculate(left)

                return [left, operation, right]

            case [list(left), ('+' | '-' | '*' | '/') as operation, list(right)]:
                left_out: Union[float, list] = Simplifier._calculate(left)
                right_out: Union[float, list] = Simplifier._calculate(right)

                output: list[Any] = [left_out, operation, right_out]

                if isinstance(left_out, list) and isinstance(right_out, list):
                    return output

                if isinstance(left_out, list) and not isinstance(right_out, list):

                    match output:
                        case [[left_left_val, left_operation, float(left_right_val)], right_operation, float(right_val)] if isinstance(left_left_val, list) or 'X' in left_left_val:
                            chain_output: Optional[list] = Simplifier._double_simplify(left_left_val, left_operation, right_operation, left_right_val, right_val)
                            if chain_output is None:
                                return output

                            return chain_output

                        case [[float(left_left_val), left_operation, left_right_val], right_operation, float(right_val)] if isinstance(left_right_val, list) or 'X' in left_right_val:
                            chain_output: Optional[list] = Simplifier._double_simplify(left_right_val, left_operation, right_operation, left_left_val, right_val)[::-1]
                            if chain_output is None:
                                return output

                            return chain_output

                        case _:
                            return output

                if not isinstance(left_out, list) and isinstance(right_out, list):

                    match output:
                        case [float(left_val), left_operation, [float(left_right_val), right_operation, right_right_val]] if isinstance(right_right_val, list) or 'X' in right_right_val:
                            chain_output: Optional[list] = Simplifier._double_simplify(right_right_val, left_operation, right_operation, left_val, left_right_val)[::-1]
                            if chain_output is None:
                                return output

                            return chain_output

                        case [float(left_val), left_operation, [left_right_val, right_operation, float(right_right_val)]] if isinstance(left_right_val, list) or 'X' in left_right_val:
                            chain_output: Optional[list] = Simplifier._double_simplify(left_right_val, left_operation, right_operation, left_val, right_right_val)
                            if chain_output is None:
                                return output

                            return chain_output

                        case _:
                            return output

                return Simplifier._calculate([left_out, operation, right_out])

            case [list(left), ('+' | '-' | '*' | '/') as operation, float(right)]:
                left_out: Union[float, list] = Simplifier._calculate(left)

                if isinstance(left_out, list):
                    output: list[Any] = [left_out, operation, right]

                    match output:
                        case [[left_left_val, left_operation, float(left_right_val)], right_operation, float(right_val)] if isinstance(left_left_val, list) or 'X' in left_left_val:
                            chain_output: Optional[list] = Simplifier._double_simplify(left_left_val, left_operation, right_operation, left_right_val, right_val)
                            if chain_output is None:
                                return output

                            return chain_output

                        case [[float(left_left_val), left_operation, left_right_val], right_operation, float(right_val)] if isinstance(left_right_val, list) or 'X' in left_right_val:
                            chain_output: Optional[list] = Simplifier._double_simplify(left_right_val, left_operation, right_operation, left_left_val, right_val)[::-1]
                            if chain_output is None:
                                return output

                            return chain_output

                        case _:
                            return output

                return Simplifier._calculate([left_out, operation, right])

            case [float(left), ('+' | '-' | '*' | '/') as operation, list(right)]:
                right_out: Union[float, list] = Simplifier._calculate(right)

                if isinstance(right_out, list):
                    output: list[Any] = [left, operation, right_out]

                    match output:
                        case [float(left_val), left_operation, [float(left_right_val), right_operation, right_right_val]] if isinstance(right_right_val, list) or 'X' in right_right_val:
                            chain_output: Optional[list] = Simplifier._double_simplify(right_right_val, left_operation, right_operation, left_val, left_right_val)[::-1]
                            if chain_output is None:
                                return output

                            return chain_output

                        case [float(left_val), left_operation, [left_right_val, right_operation, float(right_right_val)]] if isinstance(left_right_val, list) or 'X' in left_right_val:
                            chain_output: Optional[list] = Simplifier._double_simplify(left_right_val, left_operation, right_operation, left_val, right_right_val)
                            if chain_output is None:
                                return output

                            return chain_output

                        case _:
                            return output

                return Simplifier._calculate([left, operation, right_out])

            case [left, '+', right]:
                return OperatorLogic.add(left, right)

            case [left, '-', right]:
                return OperatorLogic.sub(left, right)

            case [left, '*', right]:
                return OperatorLogic.multiply(left, right)

            case [left, '/', right]:
                return OperatorLogic.divide(left, right)

            case ['sin', list(val)]:
                val: Union[float, list] = Simplifier._calculate(val)

                if isinstance(val, list):
                    return ['sin', val]

                return OperatorLogic.sin(val)

            case ['cos', list(val)]:
                val: Union[float, list] = Simplifier._calculate(val)

                if isinstance(val, list):
                    return ['cos', val]

                return OperatorLogic.cos(val)

            case [str(val)] if 'X' in val:
                return [val]

            case [list(val)]:
                return Simplifier._calculate(val)

            case [float(val)]:
                return val

            case _:
                raise ValueError(f'Invalid expression: \"{expression}\". No rule was found.')
