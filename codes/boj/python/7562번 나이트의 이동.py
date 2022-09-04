from collections import deque
import sys
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
  return list(map(_type, input().split()))

def bfs(L, start, target):
  dists = [[-1]*L for _ in range(L)]
  q = deque()

  dists[start[0]][start[1]] = 0
  q.append(start)

  while q:
    y, x = q.popleft()

    if y == target[0] and x == target[1]:
      return dists[y][x]

    for n_y, n_x in [(y-1, x-2),(y-2, x-1),(y-2, x+1),(y-1, x+2),(y+1, x-2),(y+2, x-1),(y+2, x+1),(y+1, x+2)]:
      if 0<=n_y<L and 0<=n_x<L and dists[n_y][n_x] == -1:
        dists[n_y][n_x] = dists[y][x] + 1
        q.append((n_y, n_x))


T = input(int)
for _ in range(T):
  L = input(int)
  start = input_n(int)
  target = input_n(int)

  print(bfs(L, start, target))