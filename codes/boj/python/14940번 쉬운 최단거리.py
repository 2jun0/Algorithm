import sys
from collections import deque


def input(type_=str):
    return type_(sys.stdin.readline().rstrip())


def input_n(type_):
    return list(map(type_, input().split()))


def find_start():
    for y in range(n):
        for x in range(m):
            if map[y][x] == 2:
                return y, x


dy = -1, 0, 0, 1
dx = 0, -1, 1, 0


def bfs(sy, sx):
    dists[sy][sx] = 0
    q = deque()

    q.append((sy, sx))

    while q:
        y, x = q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if not (0 <= ny < n and 0 <= nx < m):
                continue

            if map[ny][nx] == 1 and dists[ny][nx] == -1:
                dists[ny][nx] = dists[y][x] + 1
                q.append((ny, nx))


n, m = input_n(int)
map = [input_n(int) for _ in range(n)]
dists = [[-1] * m for _ in range(n)]

sy, sx = find_start()
bfs(sy, sx)

for y in range(n):
    for x in range(m):
        if dists[y][x] == -1:
            if map[y][x] == 0:
                dists[y][x] = 0
            if map[y][x] == 1:
                dists[y][x] = -1

    print(*dists[y])
