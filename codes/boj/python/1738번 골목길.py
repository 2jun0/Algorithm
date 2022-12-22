import sys
from collections import deque

def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

INF = 10**8

def bellman_ford(src):
  dist = [INF]*n
  dist[src] = 0
  parents[0] = 0
  for i in range(n):
    for a, b, d in edges:
      if dist[a] == INF:
        continue
        
      if dist[b] > dist[a] + d:
        parents[b] = a
        dist[b] = dist[a] + d
        
        if i == n-1 and visited[b]:
          return False
        
  return True

def visit_from(src):
  visited[src] = True
  q = deque()
  q.append(src)
  
  while q:
    x = q.pop()
    for nxt in graph[x]:
      if not visited[nxt]:
        q.append(nxt)
        visited[nxt] = True
 
def get_path():
  path = [n-1]
  while True:
    prev = parents[path[-1]]
    path.append(prev)
    
    if prev == 0:
      break
  
  return path[::-1]

n, m = input_n(int)
parents = [None]*n
edges = []
graph = [[] for _ in range(n)]
visited = [False]*n

for _ in range(m):
  u, v, w = input_n(int)
  edges.append((u-1, v-1, -w))
  graph[v-1].append(u-1)
visit_from(n-1)
if not bellman_ford(0):
  print(-1)
else:
  print(*[x+1 for x in get_path()])