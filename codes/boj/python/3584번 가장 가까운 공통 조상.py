import sys
from typing import Type, TypeVar

T = TypeVar("T")

sys.setrecursionlimit(20000)


def input(_type: Type[T] = str) -> T:
    return _type(sys.stdin.readline().strip())


def input_n(_type: Type[T] = str) -> list[T]:
    return list(map(_type, input().split()))


class Tree:
    def __init__(self, n: int) -> None:
        self.parents: list[int] = [-1] * (n + 1)
        self.childs: list[set[int]] = [set() for _ in range(n + 1)]
        self.levels: list[int] = [-1] * (n + 1)

    def add(self, p: int, c: int):
        self.parents[c] = p
        self.childs[p].add(c)

    def _find_root(self):
        n = len(self.parents)
        for x in range(1, n + 1):
            if self.parents[x] == -1:
                return x

        raise Exception("can't find root")

    def _propagate_level(self, x: int, level: int):
        self.levels[x] = level

        for c in self.childs[x]:
            self._propagate_level(c, level + 1)

    def calc_levels(self):
        root = self._find_root()
        self._propagate_level(root, 0)

    def get_nearest_parent(self, a: int, b: int):
        # A's level should be less than or equal b's
        if self.levels[a] > self.levels[b]:
            a, b = b, a

        ap, bp = a, b
        while self.levels[ap] < self.levels[bp]:
            bp = self.parents[bp]

        while ap != bp:
            ap = self.parents[ap]
            bp = self.parents[bp]

        return ap


t = input(int)
for _ in range(t):
    N = input(int)
    tree = Tree(N)

    for _ in range(N - 1):
        p, c = input_n(int)
        tree.add(p, c)

    tree.calc_levels()

    a, b = input_n(int)
    print(tree.get_nearest_parent(a, b))
