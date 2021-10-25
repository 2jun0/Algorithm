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

import heapq
from_root = [-1]*1000001
h = [(0,-1,N)]

while len(h) > 0:
  cnt, p, X = heapq.heappop(h)
  if from_root[X] != -1: continue
  from_root[X] = p

  if X==1: break

  if X%3 == 0: heapq.heappush(h ,(cnt+1, X, X//3))
  if X%2 == 0: heapq.heappush(h ,(cnt+1, X, X//2))
  heapq.heappush(h ,(cnt+1, X, X-1))
print(cnt)
arr = [1]
while from_root[arr[-1]] != -1:
  arr.append(from_root[arr[-1]])
print_n(arr[::-1])