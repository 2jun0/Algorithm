from collections import deque
from itertools import combinations
import sys
def input(type=str):
  return type(sys.stdin.readline().strip())
def input_n(type=str):
  return list(map(type, input().split()))

INF = 10**10
def bfs(starts):
  dists = [[INF if table[y][x] != 1 else -1 for x in range(N)] for y in range(N)]
  q = deque()

  for y,x in starts:
    dists[y][x] = 0
    q.append((y,x))

  while q:
    y, x = q.popleft()

    for ny, nx in [(y-1,x),(y+1,x),(y,x-1),(y,x+1)]:
      if 0<=ny<N and 0<=nx<N and dists[ny][nx] > dists[y][x] + 1 and table[ny][nx] != 1:
        dists[ny][nx] = dists[y][x] + 1
        q.append((ny, nx))
  
  return max([max(L) for L in dists])

N, M = input_n(int)

table = [input_n(int) for _ in range(N)]
Vs = []

for y in range(N):
  for x in range(N):
    if table[y][x] == 2:
      Vs.append((y,x))

min_time = min([bfs(Vs_case) for Vs_case in combinations(Vs, M)])  
print(min_time if min_time != INF else -1)