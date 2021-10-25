import sys
INF = 10**10
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))
def print_n(L, join_str=' '):
  for i,l in enumerate(L): print(l, end=join_str if i<len(L)-1 else '\n')
def LL(n,m,d=0): return [[d]*n for _ in range(m)]
def avg(l): return sum(l)/len(l)

N = input(int)
A = [input_n(int) for _ in range(N)]

DP = [[INF]*3 for _ in range(N)]
DP[0] = A[0]
for i in range(1, N):
  DP[i][0] = min(DP[i-1][1], DP[i-1][2]) + A[i][0]
  DP[i][1] = min(DP[i-1][0], DP[i-1][2]) + A[i][1]
  DP[i][2] = min(DP[i-1][0], DP[i-1][1]) + A[i][2]
print(min(DP[-1]))
