from dataclasses import dataclass, field
from abc import ABC, abstractmethod
from random import random


class Limiter(ABC):

    @abstractmethod
    def allow(self) -> bool:
        pass


@dataclass(slots=True)
class RandomLimiter(Limiter):
    probability: float = field(default=1.0, init=False)
    change: float = 0.8

    def allow(self) -> bool:
        self.probability *= self.change
        return random() < self.probability


@dataclass(slots=True)
class HardLimiter(Limiter):
    iterations: int = field(default=0, init=False)
    iterations_limit: int = 3

    def allow(self) -> bool:
        self.iterations += 1
        return self.iterations < self.iterations_limit


@dataclass(slots=True, init=False)
class AdaptiveLimiter(Limiter):

    def __init__(self, change: float = 0.8, iterations_limit: int = 1):
        self.random_limiter: RandomLimiter = RandomLimiter(change)
        self.hard_limiter: HardLimiter = HardLimiter(iterations_limit)

    def allow(self) -> bool:
        return self.hard_limiter.allow() and self.random_limiter.allow()
