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

n = input(int)
m = input(int)
graph = LL(0,n+1)

for _ in range(m):
  a,b,c = input_n(int)
  graph[a].append((b,c))

A,B = input_n(int)

dists = [INF]*(n+1)
parents = [0]*(n+1)

import heapq
h = []
for i, d in enumerate(dists):
  if i == A: heapq.heappush(h, (0, i, 0))
  else: heapq.heappush(h, (d, i, 0))

while len(h) > 0:
  d, x, p = heapq.heappop(h)
  if dists[x] <= d: continue
  dists[x] = d
  parents[x] = p
  for y, c in graph[x]:
    heapq.heappush(h,(dists[x]+c, y, x))

print(dists[B])
cnt = 0
path = []
x = B
while x != 0:
  path.append(x)
  x = parents[x]
  cnt += 1
print(cnt)
print_n(path[::-1])