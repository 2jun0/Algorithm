import sys
sys.setrecursionlimit(10000000) # 재귀 제한 풀기
INF = 10**10
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))
def print_n(L, join_str=' '):
  for i,l in enumerate(L): print(l, end=join_str if i<len(L)-1 else '\n')
def LL(n,m,d=0): return [[d]*n for _ in range(m)]

dp = [[0,0,0] for _ in range(10001)]
dp[1], dp[2], dp[3] = [1,0,0], [1,1,0], [1,1,1]
for i in range(4, 10001):
  dp[i][0] = dp[i-1][0]
  dp[i][1] = dp[i-2][0] + dp[i-2][1]
  dp[i][2] = dp[i-3][0] + dp[i-3][1] + dp[i-3][2]

T = input(int)
for _ in range(T):
  n = input(int)
  print(sum(dp[n]))