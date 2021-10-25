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

import heapq

N, K = input_n(int)
A = [input_n(int) for _ in range(N)]
A.sort()
C = [input(int) for _ in range(K)]
C.sort()

h = []
sum_v = 0
ai=0
for c in C:
  while ai<N and c>=A[ai][0]:
    heapq.heappush(h, (-A[ai][1], A[ai][1]))
    ai+=1
    
  if len(h) > 0:
    sum_v += heapq.heappop(h)[1]
    
print(sum_v)