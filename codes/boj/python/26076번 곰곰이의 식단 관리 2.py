import sys
from collections import deque

def input(_type=str):
  return _type(sys.stdin.readline().strip())
def input_n(_type=str):
  return list(map(_type, input().split()))

dy = [-1,-1,-1,0,0,1,1,1]
dx = [-1,0,1,-1,1,-1,0,1]

def travel(table):
  visited = [[0]*M for _ in range(N)]
  q = deque()
  # 1을 찾기 왼쪽 아래에서 출발
  for y in range(1, N):
    if table[y][0] == 1:
      q.append((y,0,1))
      visited[y][0] = 1
  for x in range(1, M-1):
    if table[N-1][x] == 1:
      q.append((N-1,x,1))
      visited[N-1][x] = 1
      
  for y in range(0, N-1):
    if table[y][M-1] == 1:
      q.append((y,M-1,2))
      visited[y][M-1] = 2
  for x in range(1, M-1):
    if table[0][x] == 1:
      q.append((0,x,2))
      visited[0][x] = 2
  
  while q:
    y, x, t = q.popleft()
    
    if visited[y][x] != t:
      return 0
    
    for ty, tx in zip(dy, dx):
      ny = y + ty
      nx = x + tx
      
      if 0<=ny<N and 0<=nx<M and table[ny][nx] == 1 and visited[ny][nx] != visited[y][x]:
        q.append((ny,nx,visited[y][x]))
        visited[ny][nx] = visited[y][x]
  
  for y in range(N):
    for x in range(M):
      if (y == 0 and x == 0) or (y == N-1 and x == M-1):
        continue
      
      ts = set()
      for ty, tx in zip(dy, dx):
        ny = y + ty
        nx = x + tx
        
        if (ny == -1 and 1 <= nx <= M) or (-1 <= ny <= N-1 and nx == M):
          ts.add(2)
        if (nx == -1 and 1 <= ny <= N) or (-1 <= nx <= M-1 and ny == N):
          ts.add(1)
        
        if 0<=ny<N and 0<=nx<M and visited[ny][nx] != 0:
          ts.add(visited[ny][nx])
      
      if len(ts) == 2:
        return 1
  return min(2, N, M)

N, M = input_n(int)
table = [input_n(int) for _ in range(N)]
print(travel(table))