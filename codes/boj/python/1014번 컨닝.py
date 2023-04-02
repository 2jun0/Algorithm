import sys

def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))  

dy = [-1, -1, 0, 0]
dx = [-1, 1, -1, 1]

C = input(int)
for _ in range(C):
  N, M = input_n(int)
  table = [''] + [input() for _ in range(N)]
  dp = [[-1]*(1<<M) for _ in range(N+1)]
  
  '''모두 없는 경우도 존재할 수 있음.'''
  for y in range(1, N+1):
    dp[y][0] = 0
  
  for y in range(1, N+1):
    for x in range(M):
      if table[y][x] != '.':
        continue
      
      # left up
      if dp[y-1][x-1] >= 0:
        dp[y][x] = dp[y-1][x-1]
        
  