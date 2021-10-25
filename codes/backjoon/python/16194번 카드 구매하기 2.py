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

N = input(int)
P = input_n(int)

dp = [INF]*(N+1)  # prices[count]
dp[0] = 0
for c, p in enumerate(P):
  for kc in range(c+1, N+1):
    dp[kc] = min(dp[kc], dp[kc-c-1] + p)
print(dp[N])
