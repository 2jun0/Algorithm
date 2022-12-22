import sys

def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

N = input(int)
A = input_n(int)

# i < j < k < l
# 0   1   2   3
# -   +   -   +

dp = [[-500_000_000]*N for _ in range(4)]
for i in range(0, N):
  dp[0][i] = max(dp[0][i-1], -A[i])
  dp[1][i] = max(dp[1][i-1], dp[0][i-1] + A[i])
  dp[2][i] = max(dp[2][i-1], dp[1][i-1] - A[i])
  dp[3][i] = max(dp[3][i-1], dp[2][i-1] + A[i])

print(dp[3][-1])