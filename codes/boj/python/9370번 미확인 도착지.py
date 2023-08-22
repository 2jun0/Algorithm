import sys
import heapq
from math import inf


def input(_type=str):
    return _type(sys.stdin.readline().strip())


def input_n(_type=str):
    return list(map(_type, input().split()))


T = input(int)

for _ in range(T):
    n, m, t = input_n(int)
    s, g, h = input_n(int)
    s, g, h = s - 1, g - 1, h - 1

    graph = [[] for _ in range(n)]

    for _ in range(m):
        a, b, d = input_n(int)
        a, b = a - 1, b - 1

        graph[a].append((d, b))
        graph[b].append((d, a))

    # find parents
    dists = [inf] * n
    parents = [[] for _ in range(n)]

    dists[s] = 0
    hq = []

    for d, nxt in graph[s]:
        dists[nxt] = d
        heapq.heappush(hq, (d, s, nxt))

    while hq:
        x_d, p, x = heapq.heappop(hq)

        if x_d != dists[x]:
            continue

        parents[x].append(p)
        if len(parents[x]) > 1:
            continue

        for d, nxt in graph[x]:
            if dists[nxt] >= dists[x] + d:
                dists[nxt] = dists[x] + d
                heapq.heappush(hq, (dists[nxt], x, nxt))

    # find routes containing g-h
    rs = [input(int) - 1 for _ in range(t)]
    found = []
    for r in rs:
        x_stack = [r]

        while x_stack:
            x = x_stack.pop()
            for p in parents[x]:
                if {p, x} == {h, g}:
                    found.append(r)
                    x_stack = []
                    break

                x_stack.append(p)

    found.sort()
    print(" ".join([str(r + 1) for r in found]))
