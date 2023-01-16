import sys
def input(_type=str):
  return _type(sys.stdin.readline().strip())
def input_n(_type=str):
  return list(map(_type, input().split()))

N = input(int)
A = input_n(int)

dp = [[0]*(N+1) for _ in range(2)]
for idx, a in enumerate(A):
  if a == 1:
    dp[0][idx+1] = dp[0][idx] + 1
    dp[1][idx+1] = min(0, dp[1][idx] + 1)
  elif a == 2:
    dp[0][idx+1] = max(0, dp[0][idx] - 1)
    dp[1][idx+1] = dp[1][idx] - 1

print(max(max(dp[0]), -min(dp[1])))

# A  : 1, 1, 2, 1, 1, 2
# dp : 1, 2, 1, 2, 3, 2
#    : 0, 0,-1, 0, 0,-1

# A  : 1, 1, 2, 2, 2, 1
# dp : 1, 2, 1, 0, 0, 1
#    : 0, 0,-1,-2,-3,-2