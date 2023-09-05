import sys


def input(type_=str):
    return type_(sys.stdin.readline().rstrip())


def input_n(type_):
    return list(map(type_, input().split()))


class UnionFindNode:
    def __init__(self):
        self.p = self

    def find(self):
        if self.p == self:
            return self

        self.p = self.p.find()
        return self.p

    def union(self, other: "UnionFindNode"):
        other.find().p = self.find()


N = input(int)
M = input(int)
nodes = [UnionFindNode() for _ in range(N)]
for a in range(N):
    can_goes = input_n(int)

    for b, can_go in enumerate(can_goes):
        if can_go == 1:
            nodes[a].union(nodes[b])

query = [num - 1 for num in input_n(int)]  # 여행 계획 도시들
parents = [nodes[idx].find() for idx in query]  # 여행 계획 도시들의 부모도시

if all(p is parents[0] for p in parents):  # 모든 부모가 같음
    print("YES")
else:
    print("NO")
