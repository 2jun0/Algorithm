import sys
from math import inf


def input(_type=str):
    return _type(sys.stdin.readline().strip())


def input_n(_type=str):
    return list(map(_type, input().split()))


V, E = input_n(int)
dists = [[inf] * V for _ in range(V)]

for _ in range(E):
    a, b, c = input_n(int)
    a, b = a - 1, b - 1
    dists[a][b] = c

for mid in range(V):
    for a in range(V):
        for b in range(V):
            dists[a][b] = min(dists[a][b], dists[a][mid] + dists[mid][b])

rs = min(dists[a][a] for a in range(V))
if rs == inf:
    print(-1)
else:
    print(rs)
