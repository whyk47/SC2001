import random

import matplotlib.pyplot as plt
from sort import hybrid_sort, merge_sort

# Time Complexity Analysis (Worst Case):
# W(S) = S(S-1)/2 for insertion sort
# W(n) = 2W(n/2) + n for merge sort
# let n = 2^k, S = 2^l, n/s = 2^(k-l)
# W(n) = 2W(n/2) + n = n + n + 4W(n/4) = ... = n*(k-l) + 2^(k-l)*W(2^l)
# = nlog(n/S) + (n/S)*(S(S-1)/2) = nlog(n) - nlog(S) + n(S-1)/2
# When n >> S, we get theta(nlog(n))


def plot(
    data: list[tuple[int, int]], xlabel: str, ylabel: str, title: str, filename: str
) -> None:
    x, y = zip(*data)
    plt.figure()
    plt.plot(x, y, marker="o")
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.grid(True)
    plt.savefig(filename)
    plt.close()


data = dict()
for i in range(3, 8):
    n = 10**i
    data[n] = [random.randint(1, n) for _ in range(n)]

cmp_vs_n = [(n, hybrid_sort(data[n].copy(), 0, len(data[n]) - 1)) for n in data]
plot(
    cmp_vs_n,
    "Array Size",
    "Number of Comparisons",
    "Hybrid Sort: Comparisons vs Array Size",
    "cmp_vs_n.png",
)
cmp_vs_s = [
    (t, hybrid_sort(data[1000000].copy(), 0, len(data[1000000]) - 1, threshold=t))
    for t in range(1, 6)
]
plot(
    cmp_vs_s,
    "Threshold Size",
    "Number of Comparisons",
    "Hybrid Sort: Comparisons vs Threshold Size",
    "cmp_vs_s.png",
)
for n, d in data.items():
    print(f"Array size: {n}")

    for t in range(5):
        print(
            f"Number of comparisons using hybrid sort (threshold={t+1}):",
            hybrid_sort(d.copy(), 0, len(d) - 1, threshold=t + 1),
        )

# Optimal S is 3
print(f"Array size: 1000000")
print(
    "Number of comparisons using merge sort:",
    merge_sort(data[1000000].copy(), 0, len(data[1000000]) - 1),
)
print(
    f"Number of comparisons using hybrid sort (threshold=3):",
    hybrid_sort(data[1000000].copy(), 0, len(data[1000000]) - 1, threshold=3),
)
