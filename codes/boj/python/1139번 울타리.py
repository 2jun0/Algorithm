import sys
from collections import deque, namedtuple
from itertools import combinations
from functools import cache


def input(_type=str):
    return _type(sys.stdin.readline().strip())


def input_n(_type=str):
    return list(map(_type, input().split()))


Line = namedtuple("Line", ["idx", "length"])


@cache
def get_size(a: Line, b: Line, c: Line):
    a, b, c = sorted((a.length, b.length, c.length))

    if c >= a + b:
        return 0

    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5


@cache
def get_bitmask(lines: list[Line]):
    return sum(1 << line.idx for line in lines)


def bfs(A: list[Line], n):
    triples = list(combinations(A, 3))

    dp = [0] * (1 << n)
    q = deque()

    for lines in triples:
        bitmask = get_bitmask(lines)
        dp[bitmask] = get_size(*lines)
        q.append((bitmask, lines))

    while q:
        cur_bitmask, lines = q.popleft()

        for nxt_lines in triples:
            triple_bitmask = get_bitmask(nxt_lines)

            if cur_bitmask & triple_bitmask > 0:
                continue

            nxt_bitmask = cur_bitmask | triple_bitmask

            if dp[nxt_bitmask] == 0:
                q.append((nxt_bitmask, nxt_lines))

            dp[nxt_bitmask] = max(
                dp[nxt_bitmask], dp[cur_bitmask] + get_size(*nxt_lines)
            )

    return max(dp)


n = input(int)
A = input_n(int)
lines = [Line(i, x) for i, x in enumerate(A)]

print(bfs(lines, n))
