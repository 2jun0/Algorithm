from collections import deque
import sys

def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

def move_bfs(visited, y, x):
  q = deque()
  q_after = deque()
  sum_v = 0
  cnt = 0

  visited[y][x] = True
  q.append((y, x))

  while q:
    y, x = q.popleft()
    q_after.append((y,x))
    sum_v += A[y][x]
    cnt += 1

    for n_y, n_x in [(y-1,x),(y+1,x),(y,x-1),(y,x+1)]:
      if 0<=n_y<N and 0<=n_x<N and not visited[n_y][n_x] and L<=abs(A[y][x]-A[n_y][n_x])<=R:
        visited[n_y][n_x] = True
        q.append((n_y,n_x))

  # after bfs
  # 인구 이동
  while q_after:
    y,x = q_after.popleft()
    A[y][x] = sum_v//cnt

  return cnt

def move_all():
  visited = [[False]*N for _ in range(N)]
  is_moved = False
  for y in range(N):
    for x in range(N):
      if not visited[y][x]:
        cnt = move_bfs(visited, y, x)
        is_moved |= cnt > 1
        
  return is_moved

N, L, R = input_n(int)

A = [input_n(int) for _ in range(N)]
day = 0
while move_all():
  day+=1

print(day)