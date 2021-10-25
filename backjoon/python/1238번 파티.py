import sys
sys.setrecursionlimit(10000000) # 재귀 제한 풀기
INF = 10**8
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))
def print_n(L, join_str=' '):
  for i,l in enumerate(L): print(l, end=join_str if i<len(L)-1 else '\n')
def LL(n,m,d=0): return [[d]*n for _ in range(m)]

N, M, X = input_n(int)
graph = LL(0,N+1)
for _ in range(M):
  a, b, c = input_n(int)
  graph[a].append((b,c))

import heapq
def func(a):
  dists = [INF]*(N+1)
  dists[a] = 0
  h = []
  for i in range(1,N+1): heapq.heappush(h, (dists[i], i, 0))
  while len(h) > 0:
    d, x, p = heapq.heappop(h)
    for y, c in graph[x]:
      if dists[y] > dists[x] + c:
        dists[y] = dists[x] + c
        heapq.heappush(h, (dists[y], y, x))
  return dists
D = func(X)
print(max([D[a]+func(a)[X] for a in range(1, N+1)]))