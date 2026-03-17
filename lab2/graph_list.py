from dataclasses import dataclass, field

from graph import Graph


@dataclass
class GraphList(Graph):
    adjacency_list: dict[int, list[tuple[int, float]]] = field(default_factory=dict)

    def __post_init__(self):
        # O(E) time to initialize the adjacency list
        for u, v, w in self.edges:
            if u not in self.adjacency_list:
                self.adjacency_list[u] = []
            self.adjacency_list[u].append((v, w))

    def distance(self, u: int, v: int) -> float:
        # O(V) time to get the distance from u to v
        for neighbor, weight in self.adjacency_list.get(u, []):
            if neighbor == v:
                return weight
        return -1

    def adj(self, u: int) -> list[int]:
        # This implementation is O(V), but it would be O(1) if we returned an iterator instead of a list
        return [v for v, _ in self.adjacency_list.get(u, [])]

    def outbound(self, u: int) -> list[tuple[int, float]]:
        # O(1) time to get the outbound edges of u
        return self.adjacency_list.get(u, [])
