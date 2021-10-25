import sys
sys.setrecursionlimit(10000000) # 재귀 제한 풀기
INF = 10**8
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))
def print_n(L, join_str=' '):
  for i,l in enumerate(L): print(l, end=join_str if i<len(L)-1 else '\n')

N = input(int)
M = input(int)
graph = [set() for _ in range(N+1)]
graph_d = [[INF for _ in range(N+1)] for _ in range(N+1)]
for _ in range(M):
  a, b, d = input_n(int)
  graph[a].add(b)
  graph_d[a][b] = min(graph_d[a][b], d)
A, B = input_n(int)

import heapq
h = []
dists = [INF]*(N+1); dists[A] = 0
for x in range(1, N+1): heapq.heappush(h ,(dists[x], x, None))
while len(h) > 0:
  ap_d, a, p = heapq.heappop(h)
  for b in graph[a]:
    if dists[b] > graph_d[a][b] + dists[a]:
      dists[b] = graph_d[a][b] + dists[a]
      heapq.heappush(h, (dists[b], b, a))
      
print(dists[B])