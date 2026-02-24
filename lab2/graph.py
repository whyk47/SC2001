from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Iterable


@dataclass
class Graph(ABC):
    vertices: int
    edges: Iterable[tuple[int, int, float]]

    @abstractmethod
    def distance(self, u: int, v: int) -> float:
        pass

    @abstractmethod
    def adj(self, u: int) -> list[int]:
        pass

    @abstractmethod
    def outbound(self, u: int) -> list[tuple[int, float]]:
        pass
