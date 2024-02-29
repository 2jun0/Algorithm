import heapq
import sys
from typing import Type, TypeVar

T = TypeVar("T")


def input(_type: Type[T] = str) -> T:
    return _type(sys.stdin.readline().strip())


def input_n(_type: Type[T] = str) -> list[T]:
    return list(map(_type, input().split()))


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def calc_max_ore(ores: list[list[int]]) -> int:
    return max(max(line) for line in ores)


def calc_max_mining_cnts(ores: list[list[int]]) -> list[int]:
    h, w = len(ores), len(ores[0])

    q: list[tuple[int, int, int]] = []
    visited = [[False] * w for _ in range(h)]

    # up
    srt_points = []
    for x in range(w):
        y = 0
        srt_points.append((y, x))
    # left
    for y in range(1, h):
        x = 0
        srt_points.append((y, x))
    # right
    for y in range(1, h):
        x = w - 1
        srt_points.append((y, x))

    for y, x in srt_points:
        heapq.heappush(q, (ores[y][x], y, x))
        visited[y][x] = True

    mining_cnts: dict[int, int] = {}
    total_mining_cnt = 0
    max_ore = 0

    while q:
        ore, y, x = heapq.heappop(q)
        total_mining_cnt += 1

        max_ore = max(max_ore, ore)
        mining_cnts[max_ore] = total_mining_cnt

        for _dx, _dy in zip(dx, dy):
            nxt_y = _dy + y
            nxt_x = _dx + x

            if nxt_y < 0 or nxt_y >= h or nxt_x < 0 or nxt_x >= w:
                continue

            if visited[nxt_y][nxt_x]:
                continue

            visited[nxt_y][nxt_x] = True
            heapq.heappush(q, (ores[nxt_y][nxt_x], nxt_y, nxt_x))

    ore2cnt = [0] * (max(mining_cnts.keys()) + 1)
    for ore in range(1, len(ore2cnt)):
        if ore in mining_cnts:
            ore2cnt[ore] = mining_cnts[ore]
        else:
            ore2cnt[ore] = ore2cnt[ore - 1]

    return ore2cnt


def search_d(max_mining_cnts: list[int], ores: list[list[int]], k: int) -> int:
    left, right = 0, calc_max_ore(ores)

    while left < right:
        mid = (left + right) // 2

        if max_mining_cnts[mid] < k:
            left = mid + 1
        else:
            right = mid

    return right


N, M, K = input_n(int)
ores = [input_n(int) for _ in range(N)]

max_mining_cnts = calc_max_mining_cnts(ores)
print(search_d(max_mining_cnts, ores, K))
