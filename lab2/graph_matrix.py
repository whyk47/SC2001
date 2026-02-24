from dataclasses import dataclass, field
from typing import Iterable

from graph import Graph


@dataclass
class GraphMatrix(Graph):
    matrix: list[list[float]] = field(init=False)

    def __post_init__(self):
        self.matrix = [[-1] * self.vertices for _ in range(self.vertices)]
        for u, v, w in self.edges:
            self.matrix[u][v] = w

        for i in range(self.vertices):
            self.matrix[i][i] = 0

    def distance(self, u: int, v: int) -> float:
        return self.matrix[u][v]

    def adj(self, u: int) -> list[int]:
        return [v for v in range(self.vertices) if self.matrix[u][v] >= 0]

    def outbound(self, u: int) -> list[tuple[int, float]]:
        return [(v, self.matrix[u][v]) for v in self.adj(u)]
