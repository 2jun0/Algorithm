import sys
sys.setrecursionlimit(100001)
def input(type=str):
  return type(sys.stdin.readline().strip())
def input_n(type=str):
  return list(map(type, input().split()))

def init_parents(p, dep, x, dist):
  depths[x] = dep
  parents[x][0] = p
  min_dists[x][0] = min(min_dists[x][0], dist)
  max_dists[x][0] = max(max_dists[x][0], dist)
  
  for child, d in adj[x]: 
    if depths[child] != -1:
      continue
    
    init_parents(x, dep+1, child, d)

def find_min_max_dist(a, b):
  if depths[a] > depths[b]:
    a, b = b, a
  
  min_d = INF
  max_d = -INF
  
  dep_diff = depths[b] - depths[a]
  k = 0
  while dep_diff > 0:
    if dep_diff % 2 == 1:
      min_d = min(min_d, min_dists[b][k])
      max_d = max(max_d, max_dists[b][k])
      b = parents[b][k]
    k += 1
    dep_diff //= 2
  
  if a != b:
    for k in range(19, -1, -1):
      if parents[a][k] != 0 and parents[a][k] != parents[b][k]:
        min_d = min(min_d, min_dists[b][k])
        max_d = max(max_d, max_dists[b][k])
        
        min_d = min(min_d, min_dists[a][k])
        max_d = max(max_d, max_dists[a][k])
        a = parents[a][k]
        b = parents[b][k]
  
      min_d = min(min_d, min_dists[b][0])
      max_d = max(max_d, max_dists[b][0])
      min_d = min(min_d, min_dists[a][0])
      max_d = max(max_d, max_dists[a][0])
  
  return min_d, max_d

INF = 10**8
N = input(int)
adj = [[] for _ in range(N+1)]
parents = [[0]*20 for _ in range(N+1)]
depths = [-1]*(N+1)
min_dists = [[INF]*20 for _ in range(N+1)]
max_dists = [[-INF]*20 for _ in range(N+1)]

for _ in range(N-1):
  A, B, C = input_n(int)
  adj[A].append((B, C))
  adj[B].append((A, C))

init_parents(0, 0, 1, 0)

for k in range(1, 20):
  for x in range(1, N+1):
    if parents[x][k-1] != 0:
      parents[x][k] = parents[parents[x][k-1]][k-1]
      min_dists[x][k] = min(min_dists[x][k-1], min_dists[parents[x][k-1]][k-1])
      max_dists[x][k] = max(max_dists[x][k-1], max_dists[parents[x][k-1]][k-1])
    
K = input(int)
for _ in range(K):
  a, b = input_n(int)
  min_d, max_d = find_min_max_dist(a, b)
  print(min_d, max_d)