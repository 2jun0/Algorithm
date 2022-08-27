from collections import deque
import sys
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

INF = 10**10
def eat_fish_bfs():
  global sy, sx, s_size, s_eat_cnt, s_move_dist

  dists = [[INF]*N for _ in range(N)]
  q = deque()

  dists[sy][sx] = 0
  q.append((sy,sx))

  candidates = []
  min_dist = INF

  while q:
    y, x = q.popleft()

    # 후보군이 나와서 깊이 제한을 걸어둠.
    if min_dist < dists[y][x]:
      break

    # 작은 물고기! 냠냠
    if table[y][x] > 0 and table[y][x] < s_size:
      candidates.append((y,x))
      min_dist = dists[y][x]
      continue

    for ny, nx in [(y-1, x), (y, x-1), (y, x+1), (y+1, x)]:
      if 0<=ny<N and 0<=nx<N and dists[ny][nx] == INF:
        # 큰 물고기!
        if table[ny][nx] > s_size:
          continue

        dists[ny][nx] = dists[y][x] + 1
        q.append((ny,nx))
  
  # 후보군이 없으면 False
  if not candidates:
    return False

  # 후보군 중에 우선순위를 y, x 정렬로 찾는다.
  candidates.sort()
  sy, sx = candidates[0]
  s_eat_cnt += 1
  table[sy][sx] = 0

  if s_eat_cnt == s_size:
    s_size += 1
    s_eat_cnt = 0

  s_move_dist += min_dist

  return True
  
N = input(int)
table = [input_n(int) for _ in range(N)]

sy, sx = -1, -1
for y in range(N):
  for x in range(N):
    if table[y][x] == 9:
      sy, sx = y, x
table[sy][sx] = 0

s_size = 2
s_eat_cnt = 0
s_move_dist = 0

while eat_fish_bfs():
  pass

print(s_move_dist)