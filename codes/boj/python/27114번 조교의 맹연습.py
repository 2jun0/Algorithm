import sys

def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

A, B, C, K = input_n(int)
INF = 10**8

dp = [[INF]*4 for _ in range(K+1)]
dp[0][0] = 0

for i in range(K+1):
  for d in range(4):
    if dp[i][d] != INF:
      for di, dd in [(A, 1), (B, 3), (C, 2)]:
        if 0<=i+di<=K:
          dp[i+di][(d+dd)%4] = min(dp[i+di][(d+dd)%4], dp[i][d]+1)
      
if dp[K][0] == INF:    
  print(-1)
else:
  print(dp[K][0])