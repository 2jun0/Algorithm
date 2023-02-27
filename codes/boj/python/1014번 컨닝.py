import sys

def input(type=str):
  return type(sys.stdin.readline().strip())
def input_n(type=str):
  return list(map(type, input().split()))

dy = [-1, -1, 0, 0]
dx = [-1, 1, -1, 1]

def dfs(A, idx):
  y, x = A[idx]
  
  if occupied[y][x] or table[y][x] == 'x':
    return 0
  
  # place 
  logs = [(y,x)]
  occupied[y][x] = True
  for i in range(4):
    ny = y + dy[i]
    nx = x + dx[i]
    
    if 0<=ny<N and 0<=nx<M and not occupied[ny][nx]:
      occupied[ny][nx] = True
      logs.append((ny,nx))
      
  # next
  max_nxt_cnt = 0
  for nidx in range(idx+1, len(A)):
    max_nxt_cnt = max(max_nxt_cnt, dfs(A, nidx))
      
  # leave
  for ly, lx in logs:
    occupied[ly][lx] = False
  
  return max_nxt_cnt + 1

C = input(int)
for _ in range(C):
  N, M = input_n(int)
  table = [input() for _ in range(N)]
  occupied = [[False]*M for _ in range(N)]
  
  A = []
  for y in range(N):
    for x in range(M):
      A.append((y,x))
  
  rs = 0
  for idx in range(len(A)):
    rs = max(rs, dfs(A,idx))
  print(rs)
