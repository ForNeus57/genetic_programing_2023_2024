from __future__ import annotations

from dataclasses import dataclass, field
from time import perf_counter

from src.genetic.evolution.population import Population


@dataclass(slots=True)
class HistoryPoint:
    generation_number: int = 0
    best: float = field(default=float('inf'))
    worst: float = field(default=float('-inf'))
    average: float = 0.
    best_program: str = ''

    def __str__(self) -> str:
        return f'[{self.generation_number}]Best: {self.best}, Worst: {self.worst}, Average: {self.average}' \
               f'\nBest program: {self.best_program}'


@dataclass(slots=True)
class Statistics:
    history: list[HistoryPoint] = field(default_factory=list, init=False)
    prev: float = perf_counter()

    def add_new_snapshot(self, population: Population, fitness_vector: tuple) -> None:
        best = (float('inf'), None)
        worst = float('-inf')

        for individual, fitness in zip(population.individuals, fitness_vector):
            if fitness < best[0]:
                best = fitness, individual
            if fitness > worst:
                worst = fitness

        point = HistoryPoint(
            len(self.history),
            best[0],
            worst,
            sum(fitness_vector) / len(fitness_vector),
            str(best[1])
        )

        self.history.append(point)
        print(point, f'Elapsed time: {perf_counter() - self.prev}')
        self.prev = perf_counter()
