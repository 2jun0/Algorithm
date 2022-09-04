from collections import deque
from itertools import combinations
import sys
def input(_type = str):
  return _type(sys.stdin.readline().strip())
def input_n(_type = str):
  return list(map(_type, input(str).split()))

INF = 10**10
def bfs(starts):
  dists = [[INF]*N for _ in range(N)]
  q = deque()

  for y, x in starts:
    dists[y][x] = 0
    q.append((y,x))
  
  while q:
    y, x = q.popleft()

    for ny, nx in [(y-1,x),(y+1,x),(y,x-1),(y,x+1)]:
      if 0<=ny<N and 0<=nx<N and table[ny][nx] != 1 and dists[ny][nx] > dists[y][x] + 1:
        dists[ny][nx] = dists[y][x] + 1
        q.append((ny,nx))

  max_dist = 0
  for y in range(N):
    for x in range(N):
      if table[y][x] == 0:
        max_dist = max(max_dist, dists[y][x])
  
  return max_dist

N, M = input_n(int)
table = [input_n(int) for _ in range(N)]
vs = []

for y in range(N):
  for x in range(N):
    if table[y][x] == 2:
      vs.append((y,x))

min_dist = INF
for starts in combinations(vs, M):
  min_dist = min(min_dist, bfs(starts))

print(-1 if min_dist == INF else min_dist)
