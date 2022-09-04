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
def getLRUD(i,j): return [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]

N = input(int)
A = []
for _ in range(N):
  h,o = input_n(int)
  h,o = min(h,o), max(h,o)
  A.append([o,h])
D = input(int)

A.sort()

import heapq
H = []
max_H_len = 0

for o,h in A:
  D_h = o - D

  heapq.heappush(H, h)

  while len(H) > 0 and H[0] < D_h:
    heapq.heappop(H)

  max_H_len = max(max_H_len, len(H))
print(max_H_len)