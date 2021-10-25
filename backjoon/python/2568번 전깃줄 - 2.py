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

def lower_bound(dp, x):
	start, end = 0, len(dp)
	mid = 0
	while start < end:
		mid = (start + end) // 2
		if x == dp[mid][1]: return mid
		elif x < dp[mid][1]: end = mid
		else:	start = mid+1
	return start


N = input(int)
A = []
P = {}
exists = {}

for _ in range(N):
	a,b = input_n(int)
	A.append((a,b))
A.sort()
for a, b in A:
	exists[a] = False

dp = []
for a, b in A:
	if len(dp) == 0:
		P[a] = (-1, -1)
		dp.append((a,b))
		continue

	if dp[-1][1] < b:
		P[a] = dp[-1]
		dp.append((a,b))
	else:
		dpi = lower_bound(dp, b)
		P[a] = dp[dpi-1] if dpi > 0 else (-1,-1)
		dp[dpi] = (a,b)

a, b = dp[-1]
while a != -1:
	exists[a] = True
	a, b = P[a]

print(len(A) - len(dp))
for a, exist in exists.items():
	if not exist: print(a)
	