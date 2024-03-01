import sys
from typing import Type, TypeVar

sys.setrecursionlimit(200000)
T = TypeVar("T")


def input(_type: Type[T] = str) -> T:
    return _type(sys.stdin.readline().strip())


def input_n(_type: Type[T] = str) -> list[T]:
    return list(map(_type, input().split()))


class Tree:
    def __init__(self, n: int, root: int, graph: list[set[int]]) -> None:
        self.parents = [-1] * (n + 1)
        self.childs = [set() for _ in range(n + 1)]
        self.subtree_sizes = [-1] * (n + 1)

        self.parents[root] = root
        self._init_tree(root, graph)

    def _init_tree(self, x: int, graph: list[set[int]]) -> None:
        for c in graph[x]:
            if self.parents[c] != -1:
                continue

            self.childs[x].add(c)
            self.parents[c] = x
            self._init_tree(c, graph)

    def get_subtree_size(self, x: int) -> int:
        if self.subtree_sizes[x] != -1:
            return self.subtree_sizes[x]

        self.subtree_sizes[x] = (
            sum(self.get_subtree_size(c) for c in self.childs[x]) + 1
        )
        return self.subtree_sizes[x]


N, R, Q = input_n(int)
graph: list[set[int]] = [set() for _ in range(N + 1)]
for _ in range(N - 1):
    U, V = input_n(int)
    graph[U].add(V)
    graph[V].add(U)

tree = Tree(N, R, graph)

for _ in range(Q):
    U = input(int)
    print(tree.get_subtree_size(U))
