from abc import ABC, abstractmethod
from dataclasses import dataclass, field


@dataclass
class MinPQ[T](ABC):
    pq: list[T] = field(default_factory=list)

    @abstractmethod
    def enqueue(self, item: T) -> None:
        pass

    @abstractmethod
    def peek(self) -> T:
        pass

    @abstractmethod
    def dequeue(self) -> T:
        pass

    @abstractmethod
    def rm_item(self, item: T) -> None:
        pass

    @abstractmethod
    def __bool__(self) -> bool:
        pass
