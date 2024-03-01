import sys
from dataclasses import dataclass
from typing import Type, TypeVar

T = TypeVar("T")


def input(_type: Type[T] = str) -> T:
    return _type(sys.stdin.readline().strip())


def input_n(_type: Type[T] = str) -> list[T]:
    return list(map(_type, input().split()))


class MaxSegTree:

    def __init__(self, n: int) -> None:
        self.n = n
        self.tree = [0] * (4 * n)
        self.lazy = [0] * (4 * n)

    def query(self, srt: int, end: int) -> int:
        return self._query(1, 0, self.n - 1, srt, end)

    def _query(self, node: int, left: int, right: int, srt: int, end: int) -> int:
        if end < left or right < srt:
            return 0

        self._propagate_lazy(node)

        if srt <= left and right <= end:
            return self.tree[node]

        mid = (left + right) // 2
        l_max = self._query(node * 2, left, mid, srt, end)
        r_max = self._query(node * 2 + 1, mid + 1, right, srt, end)

        self.tree[node] = max(self.tree[node * 2], self.tree[node * 2 + 1])
        return max(l_max, r_max)

    def add(self, srt: int, end: int, v: int):
        self._add(1, 0, self.n - 1, srt, end, v)

    def _add(self, node: int, left: int, right: int, srt: int, end: int, v: int):
        if end < left or right < srt:
            return

        self._propagate_lazy(node)

        if srt <= left and right <= end:
            self.tree[node] += v
            self.lazy[node] += v
            return

        mid = (left + right) // 2
        self._add(node * 2, left, mid, srt, end, v)
        self._add(node * 2 + 1, mid + 1, right, srt, end, v)

        self.tree[node] = max(self.tree[node * 2], self.tree[node * 2 + 1])

    def _propagate_lazy(self, node: int):
        if node * 2 < len(self.tree):
            self.tree[node * 2] += self.lazy[node]
            self.lazy[node * 2] += self.lazy[node]

            self.tree[node * 2 + 1] += self.lazy[node]
            self.lazy[node * 2 + 1] += self.lazy[node]

        self.lazy[node] = 0


class Bus:
    def __init__(self, c: int, n: int) -> None:
        self.c = c
        self.tree = MaxSegTree(n + 1)
        self._cum_people = 0

    def take(self, srt: int, end: int, people: int):
        cur_people = self.tree.query(srt, end - 1)

        remain_cap = self.c - cur_people

        taken = min(remain_cap, people)
        self._cum_people += taken

        self.tree.add(srt, end - 1, taken)

    @property
    def cum_people(self) -> int:
        return self._cum_people


@dataclass
class Group:
    srt: int
    end: int
    people: int


K, N, C = input_n(int)
bus = Bus(C, N)

groups: list[Group] = []
for _ in range(K):
    si, ei, mi = input_n(int)
    groups.append(Group(si, ei, mi))

groups.sort(key=lambda g: (g.end, g.srt))

for group in groups:
    bus.take(group.srt, group.end, group.people)

print(bus.cum_people)
