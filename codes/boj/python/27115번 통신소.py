import sys
from collections import deque
def input(_type=str):
  return _type(sys.stdin.readline().strip())
def input_n(_type=str):
  return list(map(_type, input().split()))
        
def travel(A):
  costs = [[0]*M for _ in range(N)]
  q = [deque() for _ in range(3002)]
  for p, y, x in A:
    if costs[y][x] < p:
      costs[y][x] = p
      q[p].append((y, x))
  
  for qi in range(3001, 0, -1):
    while q[qi]:
      y, x = q[qi].popleft()
      
      for dy, dx in zip((0,0,-1,1), (-1,1,0,0)):
        ny = y+dy
        nx = x+dx
        
        if 0<=ny<N and 0<=nx<M and costs[ny][nx] < costs[y][x]-1:
          costs[ny][nx] = costs[y][x]-1
          q[costs[ny][nx]].append((ny,nx))
  
  cnt = 0
  for line in costs:
    cnt += M-line.count(0)
  return cnt

N, M, K = input_n(int)

A = []
for _ in range(K):
  _y, _x, _p = input_n(int)
  A.append((_p+1, _y-1, _x-1))
print(travel(A))