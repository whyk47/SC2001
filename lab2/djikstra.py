from graph import Graph
from min_pq import MinPQ
from util import timing

"""
Adjacency Matrix + Array: 
- graph init: O(V^2) to create the matrix and fill in the edges
- pq init: O(V) to enqueue all vertices with their initial distances
- Each edge visited twice (once for each endpoint), so E enqueue and rm_item operations, each O(V) for MinPQArr
- Total: O(V^2 + V + E*V) = O((E+V)*V)

Adjacency List + Heap:
- graph init: O(E) to create the adjacency list
- pq init: O(V log V) to enqueue all vertices with their initial distances
- Each edge visited twice (once for each endpoint), so E enqueue and rm_item operations, each O(log V) for MinPQHeap
- Total: O(E + V log V + E log V) = O((E+V) log V)
"""


@timing
def djikstra(
    graph: Graph, start: int, pq: MinPQ
) -> tuple[list[float], list[int | None]]:
    d = [float("inf") for _ in range(graph.vertices)]
    pi = [None for _ in range(graph.vertices)]
    s = [False for _ in range(graph.vertices)]

    d[start] = 0
    for v in range(graph.vertices):
        # V enqueue operations, each O(log V) for MinPQHeap and O(1) for MinPQArr
        pq.enqueue((d[v], v))  # (distance, vertex)

    while pq:
        _, u = pq.dequeue()
        s[u] = True

        for v, w in graph.outbound(u):
            # E enqueue and rm_item operations, each O(log V) for MinPQHeap and O(V) for MinPQArr
            if not s[v] and d[u] + w < d[v]:
                pq.rm_item((d[v], v))
                d[v] = d[u] + w
                pi[v] = u
                pq.enqueue((d[v], v))

    return d, pi  # type: ignore


if __name__ == "__main__":
    from graph_list import GraphList
    from graph_matrix import GraphMatrix
    from min_pq_arr import MinPQArr
    from min_pq_heap import MinPQHeap

    edges = [(0, 1, 4), (0, 2, 1), (1, 2, 2), (1, 3, 5), (2, 3, 8)]
    graph = GraphList(vertices=4, edges=edges)
    print(djikstra(graph, 0, MinPQHeap()))
    graph = GraphMatrix(vertices=4, edges=edges)
    print(djikstra(graph, 0, MinPQArr()))
