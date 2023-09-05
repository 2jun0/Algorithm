import sys


def input(type_=str):
    return type_(sys.stdin.readline().rstrip())


def input_n(type_):
    return list(map(type_, input().split()))


class UnionFindNode:
    def __init__(self, num, c):
        self.num = num
        self.c = c
        self.p = self

    def find(self):
        if self.p == self:
            return self.p

        self.p = self.p.find()
        return self.p

    def union(self, node: "UnionFindNode"):
        node.find().p = self.find()


N, M, K = input_n(int)
C = input_n(int)
nodes = [UnionFindNode(idx, c) for idx, c in enumerate(C)]
for _ in range(M):
    a, b = input_n(int)
    a, b = a - 1, b - 1
    nodes[a].union(nodes[b])

costs = {}
cnts = {}
for node in nodes:
    p = node.find()
    costs[p.num] = costs.get(p.num, 0) + node.c
    cnts[p.num] = cnts.get(p.num, 0) + 1

dp = [0] * K
for key in costs.keys():
    cost, cnt = costs[key], cnts[key]

    for c in range(K - cnt - 1, -1, -1):
        dp[c + cnt] = max(dp[c + cnt], dp[c] + cost)


print(max(dp))
