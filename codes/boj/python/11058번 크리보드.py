import sys
from collections import deque

def input(_type=str):
	return _type(sys.stdin.readline().rstrip())
def input_n(_type):
	return list(map(_type, input().split()))

# cmd type
# A
# Ctrl-A, Ctrl-C, Ctrl-V
# Ctrl-V

def bfs():
  dp = [[-1]*(N+1) for _ in range(N+4)]
  qs = [deque() for _ in range(N+4)]
  dp[0][0] = 0
  qs[0].append(0)
  
  for i in range(N):
    while qs[i]:
      ci = qs[i].popleft()
      
      if dp[i+1][ci] == -1:
        qs[i+1].append(ci)
      
      # A
      dp[i+1][ci] = max(dp[i+1][ci], dp[i][ci]+1)
      # Ctrl-V
      dp[i+1][ci] = max(dp[i+1][ci], dp[i][ci] + max(dp[ci]))
      
      if dp[i+3][i] == -1:
        qs[i+3].append(i)
      
      # Ctrl-a Ctrl-c Ctrl-v
      dp[i+3][i] = max(dp[i+3][i], 2*max(dp[i]))
      
  return max(dp[N])
  

N = input(int)

print(bfs())