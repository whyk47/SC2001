import heapq
from dataclasses import dataclass, field

from min_pq import MinPQ


@dataclass
class MinPQHeap[T](MinPQ[T]):
    # Use a set to track items marked for deletion
    # * Note: This assumes items in T are hashable
    _removed: set[T] = field(default_factory=set)

    def enqueue(self, item: T) -> None:
        # O(log n)
        heapq.heappush(self.pq, item)  # type: ignore

    def _clean_heap(self) -> None:
        while self.pq and self.pq[0] in self._removed:
            item = heapq.heappop(self.pq)  # type: ignore
            self._removed.remove(item)

    def peek(self) -> T:
        # O(log n) amortized
        self._clean_heap()
        if not self.pq:
            raise IndexError("peek from an empty priority queue")
        return self.pq[0]

    def dequeue(self) -> T:
        # O(log n) amortized
        self._clean_heap()
        if not self.pq:
            raise IndexError("dequeue from an empty priority queue")
        return heapq.heappop(self.pq)  # type: ignore

    def rm_item(self, item: T) -> None:
        # O(1)
        self._removed.add(item)

    def __bool__(self) -> bool:
        return len(self.pq) > len(self._removed)
