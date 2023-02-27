import sys
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))


dp = [0]*1000001

for a in range(1,1000001):
  for k in range(a, 1000001, a):
    dp[k] += a

for k in range(1, 1000001):
  dp[k] += dp[k-1]

for _ in range(input(int)):
  n = input(int)
  print(dp[n])