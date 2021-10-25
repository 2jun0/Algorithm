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

A, B = '_'+input(), '_'+input()
dp = [[0]*len(A) for _ in range(len(B))]

for bi in range(1, len(B)):
	for ai in range(1, len(A)):
		if A[ai] == B[bi]: dp[bi][ai] = dp[bi-1][ai-1] + 1
		else: dp[bi][ai] = max(dp[bi][ai-1], dp[bi-1][ai])

lcs = ''
ai, bi = len(A)-1, len(B)-1
while ai>0 and bi>0:
	if A[ai] == B[bi]:
		lcs = A[ai]+lcs
		ai, bi = ai-1, bi-1
	elif dp[bi-1][ai] > dp[bi][ai-1]:
		bi = bi-1
	else:
		ai = ai-1

print(len(lcs))
if lcs: 
	print(lcs)
