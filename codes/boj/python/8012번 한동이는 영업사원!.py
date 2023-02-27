import sys
sys.setrecursionlimit(100001)
def input(_type=str):
	return _type(sys.stdin.readline().rstrip())
def input_n(_type):
	return list(map(_type, input().split()))

def init_parents(dep, x, p):
  depths[x] = dep
  parents[x][0] = p
  
  for child in adj[x]:
    if depths[child] == -1:
      init_parents(dep+1, child, x)

def update_parents():
  for k in range(1, 20):
    for x in range(1, N+1):
      if parents[x][k-1] != 0:
        parents[x][k] = parents[parents[x][k-1]][k-1]

def get_dist(a, b):
  if depths[a] > depths[b]:
    a, b = b, a
    
  dist = 0
  dep_diff = depths[b] - depths[a]
  k = 0
  while dep_diff > 0:
    if dep_diff % 2 == 1:
      dist += 2**k
      b = parents[b][k]
      
    dep_diff >>= 1
    k += 1
  
  if a != b:
    for k in range(19, -1, -1):
      if parents[a][k] != 0 and parents[a][k] != parents[b][k]:
        a = parents[a][k]
        b = parents[b][k]
        dist += (2**k) * 2
    
    dist += 2
  
  return dist

N = input(int)
adj = [[] for _ in range(N+1)]
depths = [-1]*(N+1)
parents = [[0]*20 for _ in range(N+1)]

for _ in range(N-1):
  a, b = input_n(int)
  adj[a].append(b)
  adj[b].append(a)

init_parents(0, 1, 0)
update_parents()

dist = 0
m = input(int)
cur = 1
for _ in range(m):
  nxt = input(int)
  dist += get_dist(cur, nxt)
  cur = nxt
  
print(dist)