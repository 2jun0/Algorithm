import sys

def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

N = input(int)
K = input(int)

def get_case_cnt(first):
  dp = [[[0]*2 for _ in range(K+1)] for _ in range(N)]

  if first:
    dp[0][1][1] = 1
  else:
    dp[0][0][0] = 1

  for i in range(1,N):
    for k in range(K+1):
      # 선택함
      if k-1 >= 0:
        dp[i][k][1] += dp[i-1][k-1][0]
        dp[i][k][1] %= 1_000_000_003
      # 안함
      dp[i][k][0] += dp[i-1][k][0]
      dp[i][k][0] += dp[i-1][k][1]
      dp[i][k][0] %= 1_000_000_003

  if first:
    return dp[-1][-1][0]
  else:
    return sum(dp[-1][-1])

print((get_case_cnt(True) + get_case_cnt(False)) % 1_000_000_003)