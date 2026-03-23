def unbounded_knapsack(
    C: int, weights: list[int], profits: list[int]
) -> tuple[list[int], list[int]]:
    n: int = len(weights)
    P: list[int] = [0] * (C + 1)
    chosen: list[int] = [-1] * (
        C + 1
    )  # tracks which item gave the best profit at capacity c

    for c in range(1, C + 1):
        for i in range(n):
            if weights[i] <= c:
                candidate: int = profits[i] + P[c - weights[i]]
                if candidate > P[c]:
                    P[c] = candidate
                    chosen[c] = i

    return P, chosen


def trace_solution(C: int, weights: list[int], chosen: list[int]) -> list[int]:
    """Trace back which objects were packed."""
    items: list[int] = []
    c: int = C
    while c > 0 and chosen[c] != -1:
        i: int = chosen[c]
        items.append(i)
        c -= weights[i]
    return items


def print_dp_table(P: list[int], C: int) -> None:
    """Print the DP table."""
    print(f"\n  {'c':>4} | {'P(c)':>6}")
    print("  " + "-" * 14)
    for c in range(C + 1):
        print(f"  {c:>4} | {P[c]:>6}")


def run_case(label: str, C: int, weights: list[int], profits: list[int]) -> None:
    print("=" * 55)
    print(f"  {label}")
    print("=" * 55)
    print(f"  Capacity C = {C}")
    print(f"  Weights  : {weights}")
    print(f"  Profits  : {profits}")

    P, chosen = unbounded_knapsack(C, weights, profits)

    print_dp_table(P, C)

    items = trace_solution(C, weights, chosen)
    from collections import Counter

    item_counts = Counter(items)

    print(f"\n  Maximum Profit P({C}) = {P[C]}")
    print(f"  Objects packed:")
    total_w = 0
    total_p = 0
    for i, count in sorted(item_counts.items()):
        w = weights[i] * count
        p = profits[i] * count
        total_w += w
        total_p += p
        print(
            f"    Object type {i}: {count}x  "
            f"(weight={weights[i]}, profit={profits[i]})  "
            f"-> total weight={w}, total profit={p}"
        )
    print(f"  Total weight used: {total_w} / {C}")
    print(f"  Total profit     : {total_p}")
    print()


# ── Case (a): weights=[4,6,8], profits=[7,6,9] ──────────────────────────────
run_case(
    label="Case (a): w=[4,6,8], p=[7,6,9]",
    C=14,
    weights=[4, 6, 8],
    profits=[7, 6, 9],
)

# ── Case (b): weights=[5,6,8], profits=[7,6,9] ──────────────────────────────
run_case(
    label="Case (b): w=[5,6,8], p=[7,6,9]",
    C=14,
    weights=[5, 6, 8],
    profits=[7, 6, 9],
)
