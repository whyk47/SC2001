from dataclasses import dataclass, field

from graph import Graph


@dataclass
class GraphList(Graph):
    adjacency_list: dict[int, list[tuple[int, float]]] = field(default_factory=dict)

    def __post_init__(self):
        for u, v, w in self.edges:
            if u not in self.adjacency_list:
                self.adjacency_list[u] = []
            self.adjacency_list[u].append((v, w))

    def distance(self, u: int, v: int) -> float:
        for neighbor, weight in self.adjacency_list.get(u, []):
            if neighbor == v:
                return weight
        return -1

    def adj(self, u: int) -> list[int]:
        return [v for v, _ in self.adjacency_list.get(u, [])]

    def outbound(self, u: int) -> list[tuple[int, float]]:
        return self.adjacency_list.get(u, [])
