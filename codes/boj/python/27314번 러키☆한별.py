import sys
from collections import deque

def input(type=str):
  return type(sys.stdin.readline().strip())
def input_n(type=str):
  return list(map(type, input().split()))

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]

def get_exists_dist(sy, sx):
  dists = [[-1]*M for _ in range(N)]
  q = deque()
  
  dists[sy][sx] = 0
  q.append((sy, sx))
  
  exits = []
  
  while q:
    y, x = q.popleft()
    
    if table[y][x] == '#':
      exits.append((y,x,dists[y][x]))
    
    for i in range(4):
      ny = y + dy[i]
      nx = x + dx[i]
      
      if 0<=ny<N and 0<=nx<M and table[ny][nx] != 'X' and dists[ny][nx] == -1:
        dists[ny][nx] = dists[y][x] + 1
        q.append((ny, nx))
  
  return exits

def get_dists_to_exits(sy, sx, exists):
  dists = [[-1]*M for _ in range(N)]
  q = deque()
  
  dists[sy][sx] = 0
  q.append((sy, sx))
  
  exits_idx = [[-1]*M for _ in range(N)]
  for i, pos in enumerate(exists):
    y, x, _ = pos
    exits_idx[y][x] = i
  
  dist_by_exits = [-1]*len(exists)
  
  while q:
    y, x = q.popleft()
    
    if exits_idx[y][x] != -1:
      dist_by_exits[exits_idx[y][x]] = dists[y][x]
    
    for i in range(4):
      ny = y + dy[i]
      nx = x + dx[i]
      
      if 0<=ny<N and 0<=nx<M and table[ny][nx] != 'X' and dists[ny][nx] == -1:
        dists[ny][nx] = dists[y][x] + 1
        q.append((ny, nx))
  
  return dist_by_exits

N, M = input_n(int)
table = [input(str) for _ in range(N)]

P = []
H = None
for y in range(N):
  for x in range(M):
    if table[y][x] == 'H':
      H = (y, x)
    if table[y][x] == 'P':
      P.append((y,x))
      
exits = get_exists_dist(*H)
give_cnt = [0]*len(exits)
for y, x in P:
  dists = get_dists_to_exits(y, x, exits)
  for i, d in enumerate(dists):
    if exits[i][2] >= d and d != -1:
      give_cnt[i] += 1
      
print(max(give_cnt))