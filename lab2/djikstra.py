from graph import Graph
from min_pq import MinPQ
from util import timing

"""
Adjacency Matrix + Array: 
- graph init: theta(V^2) to create the matrix and fill in the edges
- pq init: theta(V) to enqueue all vertices with their initial distances
- Each vertex visited once, so V dequeue operations (theta(V))
- Each edge visited twice (once for each endpoint), so E enqueue (theta(1)) and rm_item operations (theta(V))
- Total: theta(V^2 + 2V + E*(V+1)) = theta((E+V)*V)

Adjacency List + Heap:
- graph init: theta(E) to create the adjacency list
- pq init: theta(V log V) to enqueue all vertices with their initial distances
- Each vertex visited once, so V dequeue operations, each theta(log V) amortized
- Each edge visited twice (once for each endpoint), so E enqueue theta(log V) and rm_item operations (theta(1))
- Total: theta(E + 2V log V + 2E (log V + 1)) = theta((E+V) log V)
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
        # V enqueue operations, each theta(log V) for MinPQHeap and theta(1) for MinPQArr
        pq.enqueue((d[v], v))  # (distance, vertex)

    while pq:
        _, u = pq.dequeue()
        s[u] = True

        for v, w in graph.outbound(u):
            # E enqueue and rm_item operations, each theta(log V) for MinPQHeap and theta(V) for MinPQArr
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
