from dataclasses import dataclass, field

from min_pq import MinPQ


@dataclass
class MinPQArr[T](MinPQ[T]):
    pq: list[T] = field(default_factory=list)

    def enqueue(self, item: T) -> None:
        # theta(1)
        self.pq.append(item)

    def get_ind(self) -> int:
        # theta(n)
        if not self.pq:
            return -1
        ind = 0
        smallest = self.pq[0]
        for i in range(len(self.pq)):
            if self.pq[i] < smallest:  # type: ignore
                smallest = self.pq[i]
                ind = i
        return ind

    def peek(self) -> T:
        # theta(n)
        ind = self.get_ind()
        if ind != -1:
            return self.pq[ind]
        raise IndexError("peek from empty MinPQ")

    def dequeue(self) -> T:
        # theta(n)
        ind = self.get_ind()
        if ind != -1:
            return self.pq.pop(ind)
        raise IndexError("dequeue from empty MinPQ")

    def rm_item(self, item: T) -> None:
        # theta(n)
        for i in range(len(self.pq)):
            if self.pq[i] == item:
                self.pq.pop(i)
                return

    def __bool__(self) -> bool:
        return bool(self.pq)
