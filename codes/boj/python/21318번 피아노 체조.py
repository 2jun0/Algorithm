import sys

def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

def get_mistake_dp(Lv):
  dp = [0]*len(Lv)
  for i in range(1, len(Lv)):
    if Lv[i-1] > Lv[i]:
      dp[i] = dp[i-1] + 1
    else:
      dp[i] = dp[i-1]
  return dp

N = input(int)
Lv = input_n(int)

Q = input(int)
dp = get_mistake_dp(Lv)
for _ in range(Q):
  s, e = input_n(int)
  print(dp[e-1] - dp[s-1])