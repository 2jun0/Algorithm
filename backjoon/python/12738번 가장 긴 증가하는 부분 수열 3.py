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

def lower_bound(A, x):
	start, end = 0, len(A)
	while start < end:
		mid = (start + end)//2
		if x <= A[mid]: end = mid
		else: start = mid+1
	return start


N = input(int)
A = input_n(int)

dp = []
for a in A:
	idx = lower_bound(dp, a)
	if idx >= len(dp): dp.append(a)
	else: dp[idx] = a
print(len(dp))