import sys
from math import inf


def input(type_=str):
    return type_(sys.stdin.readline().rstrip())


def input_n(type_):
    return list(map(type_, input().split()))


N, M = input_n(int)
graph = [[] for _ in range(N)]
dists = [inf] * N
dists[0] = 0

for _ in range(M):
    A, B, C = input_n(int)
    A -= 1
    B -= 1

    graph[A].append((B, C))


for _ in range(N - 1):
    for x in range(N):
        for y, d in graph[x]:
            dists[y] = min(dists[x] + d, dists[y])

flag = False
for x in range(N):
    for y, d in graph[x]:
        flag |= dists[x] + d < dists[y]

if flag:
    print(-1)
else:
    for y in range(1, N):
        if dists[y] >= inf:
            print(-1)
            continue

        print(dists[y])
