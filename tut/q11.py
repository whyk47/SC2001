from collections.abc import MutableSequence
from itertools import permutations
from typing import Iterable

adj = [[0 for _ in range(8)] for _ in range(8)]
edges = [(2, 3), (2, 7), (3, 1), (7, 1), (7, 6), (6, 0), (1, 0), (1, 4), (4, 5)]
for u, v in edges:
    adj[u][v] = 1
vertices = [i for i in range(8)]


def is_valid_seq(seq: Iterable[int]) -> bool:
    index_of = [0 for _ in range(8)]
    for i, v in enumerate(seq):
        index_of[v] = i
    for u, v in edges:
        if index_of[u] > index_of[v]:
            return False
    return True


sequences = permutations(vertices)

n = 0
for seq in sequences:
    if is_valid_seq(seq):
        n += 1
print(n)
# 21

visited = set()


def dfs(seq: MutableSequence[int]) -> int:
    if not is_valid_seq(seq) or tuple(seq) in visited:
        return 0
    n = 1
    visited.add(tuple(seq))
    for i in range(7):
        new_seq = seq[:]
        new_seq[i], new_seq[i + 1] = new_seq[i + 1], new_seq[i]
        n += dfs(new_seq)
    return n


# [C,H,D,B,E,F,G,A]
seq = [2, 7, 3, 1, 4, 5, 6, 0]

print(dfs(seq))
