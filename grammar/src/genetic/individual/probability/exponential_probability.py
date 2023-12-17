from typing import Generator


class ExponentialProbability(Generator):
    """
    TODO: Make use of numpy.random.exponential
    """
    __slots__ = ('base_probability', 'common_ratio')

    def __init__(self, base_probability: float = 1.0, common_ration: float = 0.8):
        if 0.0 > base_probability or 1.0 < base_probability:
            raise ValueError(f"Base probability must be between 0.0 and 1.0, inclusive. Received {base_probability}.")

        if 0.0 > common_ration or 1.0 < common_ration:
            raise ValueError(
                f"Probability scaler must be between 0.0 and 1.0, inclusive. Received {common_ration}.")

        self.probability: float = base_probability
        self.common_ratio: float = common_ration

    def send(self, _):
        output: float = self.probability
        self.probability *= self.common_ratio
        return output

    def throw(self, __typ, __val=..., __tb=...):
        raise StopIteration
