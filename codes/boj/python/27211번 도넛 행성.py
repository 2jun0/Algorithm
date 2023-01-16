import sys
from collections import deque
def input(_type=str):
  return _type(sys.stdin.readline().strip())
def input_n(_type=str):
  return list(map(_type, input().split()))

def bfs(sy, sx, visited):
  q = deque()
  
  visited[sy][sx] = True
  q.append((sy, sx))
  
  while q:
    y, x = q.popleft()
    
    for dy, dx in zip([0,0,-1,1], [-1,1,0,0]):
      ny = (y + dy) % N
      nx = (x + dx) % M
      
      if not visited[ny][nx] and table[ny][nx] == 0:
        visited[ny][nx] = True
        q.append((ny,nx))

N, M = input_n(int)
table = [input_n(int) for _ in range(N)]
visited = [[False]*M for _ in range(N)]
cnt = 0
for y in range(N):
  for x in range(M):
    if not visited[y][x] and table[y][x] == 0:
      cnt += 1
      bfs(y,x,visited)
      
print(cnt)