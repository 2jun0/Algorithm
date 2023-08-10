import sys
from collections import deque


def input(type_=str):
    return type_(sys.stdin.readline().rstrip())


def input_n(type_):
    return list(map(type_, input().split()))


def bfs(sy, sx):
    q = deque()
    visited = [[False] * M for _ in range(N)]
    q.append((sy, sx))
    visited[sy][sx] = True

    cnt = 0

    while q:
        y, x = q.popleft()

        if table[y][x] == "P":
            cnt += 1

        for ny, nx in [(y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)]:
            if not (0 <= ny < N and 0 <= nx < M):
                continue
            if visited[ny][nx]:
                continue

            if table[ny][nx] != "X":
                q.append((ny, nx))
                visited[ny][nx] = True

    return cnt


def start():
    for y in range(N):
        for x in range(M):
            if table[y][x] == "I":
                return y, x


N, M = input_n(int)
table = [input() for _ in range(N)]
sy, sx = start()

rs = bfs(sy, sx)

if rs == 0:
    print("TT")
else:
    print(rs)
