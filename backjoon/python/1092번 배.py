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
A.sort()
M = input(int)
B = input_n(int)
B.sort()

if A[-1] < B[-1]:
  print(-1)
else:
  ai = N-1
  ABI = [-1]*N
  for bi in range(M-1, -1, -1):
    if B[bi] <= A[ai]:
      ABI[ai] = bi
      ai-=1
    
    if ai < 0: break

  cnt = 0
  while len(B) > 0:
    for ai in range(N-1, -1, -1):
      ab_i = min(ABI[ai], len(B)-1)
      while ab_i >= 0 and B[ab_i] > A[ai]:
        ab_i -= 1
      if ab_i == -1: continue

      del B[ab_i]
      if len(B) == 0: break

    cnt += 1
  print(cnt)

  