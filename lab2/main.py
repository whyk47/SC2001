from itertools import permutations
from random import randint, sample

from djikstra import djikstra
from graph_list import GraphList
from graph_matrix import GraphMatrix
from min_pq_arr import MinPQArr
from min_pq_heap import MinPQHeap

EDGE_FRACTIONS = [0.25, 0.5, 0.75, 1.0]
sizes = range(400, 2001, 400)


def generate_graphs() -> dict[int, dict[float, list[tuple[int, int, int]]]]:
    generated = {
        n: {f: [] for f in EDGE_FRACTIONS} for n in sizes
    }  # Store generated graphs for each vertex count and edge fraction

    for n in sizes:
        for frac in EDGE_FRACTIONS:
            possible_edges = list(permutations(range(n), 2))
            if frac == 1.0:
                chosen = possible_edges
            else:
                chosen = sample(possible_edges, int(frac * len(possible_edges)))
            edges = [(u, v, randint(1, n)) for u, v in chosen]
            generated[n][frac] = edges
            print(
                f"Vertices: {n}, Edge Fraction: {frac}, Number of Edges: {len(edges)}"
            )
            print(f"Sample Edges: {edges[:5]}")
    return generated


print("Generating graphs...")
graphs = generate_graphs()
print("Graphs generated.")
print()

for n in sizes:
    for f in EDGE_FRACTIONS:
        print(f"Vertices: {n}, Edge Fraction: {f}")
        graph_list = GraphList(vertices=n, edges=graphs[n][f])
        graph_matrix = GraphMatrix(vertices=n, edges=graphs[n][f])
        print("Running Dijkstra with MinPQHeap on GraphList...")
        djikstra(graph_list, 0, MinPQHeap())
        print("Running Dijkstra with MinPQArr on GraphMatrix...")
        djikstra(graph_matrix, 0, MinPQArr())
