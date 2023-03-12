import sys

def input(_type=str):
  return _type(sys.stdin.readline().strip())
def input_n(_type=str):
  return list(map(_type, input().split()))

N, M = input_n(int)
dp = [10_000_000] * (N+1)
dp[0] = 0
for _ in range(M):
  pp, p = input_n(int)
  
  for i in range(N+1):
    if dp[i] == 10_000_000: continue
    
    for j, v in zip([i+1, i+6], [p, pp]):
      nxt = min(j, N)
      dp[nxt] = min(dp[nxt], dp[i] + v)

print(dp[N])