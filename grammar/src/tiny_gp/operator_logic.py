"""
Module that models the operations from original TinyGP, should only be used when we try to model the input / output to
TinyGP.java algorithm.

This module contains the following classes:

- `OperatorLogic`: A custom class that mimics TinyGP way of arithmetic.

.. note:: This module is specifically designed for compatibility with the original TinyGP and should only be used
when trying to model the input/output to the TinyGP.java algorithm.
"""

from typing import Final
from math import sin, cos


class OperatorLogic:
    """
    This is a custom class that mimics TinyGP way of arithmetic.

    Attributes
    ----------
    division_threshold : float
        A threshold for division operation to avoid division by zero.

    Methods
    -------
    add(x: float, y: float) -> float
        Adds two numbers.

    sub(x: float, y: float) -> float
        Subtracts two numbers.

    multiply(x: float, y: float) -> float
        Multiplies two numbers.

    divide(x: float, y: float) -> float
        Divides two numbers with a threshold to avoid division by zero.

    sin(x: float) -> float
        Returns the sine of a number.

    cos(x: float) -> float
        Returns the cosine of a number.
    """

    division_threshold: Final[float] = 0.001

    @staticmethod
    def add(x: float, y: float) -> float:
        """
        Adds two numbers.

        Parameters
        ----------
        x : float
            The first number.
        y : float
            The second number.

        Returns
        -------
        float
            The sum of x and y.
        """
        return x + y

    @staticmethod
    def sub(x: float, y: float) -> float:
        """
        Subtracts two numbers.

        Parameters
        ----------
        x : float
            The first number.
        y : float
            The second number.

        Returns
        -------
        float
            The result of x - y.
        """
        return x - y

    @staticmethod
    def multiply(x: float, y: float) -> float:
        """
        Multiplies two numbers.

        Parameters
        ----------
        x : float
            The first number.
        y : float
            The second number.

        Returns
        -------
        float
            The product of x and y.
        """
        return x * y

    @staticmethod
    def divide(x: float, y: float) -> float:
        """
        Divides two numbers with a threshold to avoid division by zero.

        Parameters
        ----------
        x : float
            The numerator.
        y : float
            The denominator.

        Returns
        -------
        float
            The result of x / y if x is greater than the division threshold, else y.
        """
        return x / y if abs(x) > OperatorLogic.division_threshold else y

    @staticmethod
    def sin(x: float) -> float:
        """
        Returns the sine of a number.

        Parameters
        ----------
        x : float
            The number.

        Returns
        -------
        float
            The sine of x.
        """
        return sin(x)

    @staticmethod
    def cos(x: float) -> float:
        """
        Returns the cosine of a number.

        Parameters
        ----------
        x : float
            The number.

        Returns
        -------
        float
            The cosine of x.
        """
        return cos(x)
