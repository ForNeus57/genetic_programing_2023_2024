"""
subsequent_node_probability_generator
-------------------------------------

This module contains the SubsequentNodeProbabilityGenerator class which is used to generate subsequent node probabilities.
The probability is decreased exponentially for each generation.

Classes
-------
SubsequentNodeProbabilityGenerator
    A class used to generate subsequent node probabilities. The probability is decreased exponentially for each
    generation.

    Attributes
    ----------
    probability : float
        the base probability for the first node
    probability_scaler : float
        the factor by which the probability is scaled down for each subsequent node

    Methods
    -------
    __next__():
        Yields the current probability and scales it down for the next node.
"""


class SubsequentNodeProbabilityGenerator:
    """
    A class used to generate subsequent node probabilities. The probability is decreased exponentially for each
    generation.

    ...

    Attributes
    ----------
    probability : float
        the base probability for the first node
    probability_scaler : float
        the factor by which the probability is scaled down for each subsequent node

    Methods
    -------
    __next__():
        Yields the current probability and scales it down for the next node.
    """

    def __init__(self, base_probability: float = 1.0, probability_scaler: float = 0.9):
        """
        Constructs a new SubsequentNodeProbabilityGenerator.

        Parameters
        ----------
        base_probability : float, optional
            the base probability for the first node (default is 1.0)
        probability_scaler : float, optional
            the factor by which the probability is scaled down for each subsequent node (default is 0.9)

        Raises
        ------
        ValueError
            If base_probability or probability_scaler is not between 0.0 and 1.0, inclusive.
        """
        if 0.0 <= base_probability <= 1.0:
            raise ValueError(f"Base probability must be between 0.0 and 1.0, inclusive. Received {base_probability}.")

        if 0.0 <= probability_scaler <= 1.0:
            raise ValueError(
                f"Probability scaler must be between 0.0 and 1.0, inclusive. Received {probability_scaler}.")

        self.probability: float = base_probability
        self.probability_scaler: float = probability_scaler

    def __next__(self):
        """
        Yields the current probability and scales it down for the next node.

        Yields
        ------
        float
            The current probability.
        """
        yield self.probability
        self.probability *= self.probability_scaler
