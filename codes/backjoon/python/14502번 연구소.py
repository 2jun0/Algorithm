from collections import deque
import sys

def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

N, M = input_n(int)
table = [input_n(int) for _ in range(N)]

def bfs():
  s = deque()
  can_visit = [[True] * M for _ in range(N)]

  for y in range(N):
    for x in range(M):
      if table[y][x] == 2:
        can_visit[y][x] = False
        s.append((y,x))
      elif table[y][x] == 1:
        can_visit[y][x] = False

  while s:
    y, x = s.popleft()
    for n_y, n_x in [(y-1,x), (y+1,x), (y,x-1), (y,x+1)]:
      if 0<=n_y<N and 0<=n_x<M and can_visit[n_y][n_x]:
        s.append((n_y,n_x))
        can_visit[n_y][n_x] = False

  return sum([sum(L) for L in can_visit])

def make_wall(lv, pos_idx):
  global max_cnt

  if lv == 3:
    max_cnt = max(max_cnt, bfs())
    return
  
  for n_idx in range(pos_idx+1, len(make_wall.poses)):
    n_y, n_x = make_wall.poses[n_idx]

    if table[n_y][n_x] == 0:
      table[n_y][n_x] = 1
      make_wall(lv+1, n_idx)
      table[n_y][n_x] = 0

make_wall.poses = [(y,x) for x in range(M) for y in range(N)]

max_cnt = -1
make_wall(0, -1)

print(max_cnt)
