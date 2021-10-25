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
def avg(l): return sum(l)/len(l)

N = input(int)
A = input_n(int)

dp = []
def bsearch(start, end, x):
  while start < end:
    mid = (start+end)//2
    if x <= A[dp[mid]]: end = mid
    else: start = mid+1
  return start

before = [-1]*N
for ai, a in enumerate(A):
  i = bsearch(0, len(dp), a)
  if len(dp) <= i: dp.append(ai)
  else: dp[i] = ai
  if i > 0: before[ai] = dp[i-1]

print(len(dp))

LIS = []
i = dp[-1]
while i != -1: 
  LIS=[A[i]]+LIS
  i = before[i]
print_n(LIS)
