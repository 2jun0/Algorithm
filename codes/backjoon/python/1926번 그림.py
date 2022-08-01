from collections import deque
import sys
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
  return list(map(_type, input().split()))

n, m = input_n(int)
table = [input_n(int) for _ in range(n)]
parents = [[-1]*m for _ in range(n)]

def bfs(start,v):
  parents[start[0]][start[1]] = v
  q = deque([start])

  cnt = 0
  while q:
    y, x = q.popleft()
    cnt += 1

    for n_y, n_x in [(y+1, x),(y-1, x),(y, x+1),(y, x-1)]:
      if 0<=n_y<n and 0<=n_x<m and table[n_y][n_x] == 1 and parents[n_y][n_x] == -1:
        parents[n_y][n_x] = v
        q.append((n_y, n_x))

  return cnt

union_cnt = 0
max_bfs = 0
for y in range(n):
  for x in range(m):
    if table[y][x] == 1 and parents[y][x] == -1:
      union_cnt += 1
      max_bfs = max(max_bfs, bfs((y,x), union_cnt))

print(union_cnt)
print(max_bfs)