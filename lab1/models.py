from dataclasses import dataclass
from typing import Any, Callable, Protocol, Self, overload


class Comparable(Protocol):
    def __lt__(self, other: Self) -> bool: ...


@dataclass(order=True)
class Student:
    name: str
    cgpa: float


if __name__ == "__main__":

    def cmp[T: Comparable](
        a: T, b: T, key: Callable[[T, T], float] | None = None
    ) -> float:
        if key is not None:
            return key(a, b)

        if a < b:
            return -1
        if a > b:
            return 1
        return 0

    s1 = Student("Alice", 3.7)
    s2 = Student("Bob", 3.5)
    print(cmp(s1, s2))
    print(cmp(s1, s2, key=lambda a, b: a.cgpa - b.cgpa))
