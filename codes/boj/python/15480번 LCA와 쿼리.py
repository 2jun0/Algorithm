import sys
sys.setrecursionlimit(100001)
def input(_type=str):
	return _type(sys.stdin.readline().rstrip())
def input_n(_type):
	return list(map(_type, input().split()))

def init_parents(x, dep, p):
  depths[x] = dep
  parents[x][0] = p
  
  for child in adj[x]:
    if depths[child] == -1:
      init_parents(child, dep+1, x)
  
def update_parents():
  for k in range(1, 20):
    for x in range(1, N+1):
      if parents[x][k-1] != 0:
        parents[x][k] = parents[parents[x][k-1]][k-1]

def find_LCA(a, b):
  if depths[a] > depths[b]:
    a, b = b, a
    
  if depths[b] > depths[a]:
    dep_diff = depths[b] - depths[a]
    k = 0
    
    while dep_diff > 0:
      if dep_diff % 2 == 1:
        b = parents[b][k]
        
      k += 1
      dep_diff >>= 1
  
  if a != b:
    for k in range(19, -1, -1):
      if parents[a][k] != 0 and parents[a][k] != parents[b][k]:
        a = parents[a][k]
        b = parents[b][k]
        
    a = parents[a][0]
    b = parents[b][0]
  
  return a

def query(root, a, b):
  rs = 0
  
  for x, y in [(root, a), (root, b), (a, b)]:
    lca = find_LCA(x, y)
    if depths[rs] < depths[lca]:
      rs = lca
  return rs

N = input(int)
parents = [[0]*20 for _ in range(N+1)]
depths = [-1]*(N+1)
adj = [[] for _ in range(N+1)]

for _ in range(N-1):
  a, b = input_n(int)
  adj[a].append(b)
  adj[b].append(a)

init_parents(1, 0, 0)
update_parents()

M = input(int)
for _ in range(M):
  root, a, b = input_n(int)
  print(query(root, a, b))