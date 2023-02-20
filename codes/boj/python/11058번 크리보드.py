import sys
from collections import defaultdict

def input(_type=str):
	return _type(sys.stdin.readline().rstrip())
def input_n(_type):
	return list(map(_type, input().split()))

# cmd type
# A
# Ctrl-A, Ctrl-C
# Ctrl-V

N = input(int)

# (turn, 복사 위치 기본이 0 없음)
dp = [[-1]*(N+1) for _ in range(N+4)]
dp[0][0] = 0
for i in range(0, N):
  # A
  for ci in range(N):
    if dp[i][ci] == -1: continue
    
    dp[i+1][ci] = max(dp[i+1][ci], dp[i][ci]+1)
  
  for ci in range(N):
    if dp[i][ci] == -1: continue
    # Ctrl-V
    dp[i+1][ci] = max(dp[i+1][ci], dp[i][ci] + max(dp[ci]))
  # Ctrl-a Ctrl-c Ctrl-vf
  dp[i+3][i] = max(dp[i+3][i], 2*max(dp[i]))

print(max(dp[N]))