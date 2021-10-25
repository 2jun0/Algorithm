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

def bsearch(A, x):
  start, end = 0, len(A)
  while start < end:
    mid = (start+end)//2
    if x > A[mid]:
      start = mid+1
    else:
      end = mid
  return start

dp = [A[0]]
for a in A[1:]:
  idx = bsearch(dp, a)
  if len(dp) <= idx: dp.append(a)
  else: dp[idx] = a

print(len(dp))