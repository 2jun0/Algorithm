import sys
sys.setrecursionlimit(200001)

def input(type=str):
  return type(sys.stdin.readline().strip())
def input_n(type=str):
  return list(map(type, input().split()))

def switch(p, c):
  childs[p].remove(c)
  childs[c].add(p)
  parent[c] = parent[p]
  parent[p] = c
  
  cnts[p] -= cnts[c]
  cnts[c] += cnts[p]

def init_childs(x, p):
  initialized[x] = True
  childs[p].add(x)
  parent[x] = p
  cnts[x] = 1
  for ch in adj[x]:
    if not initialized[ch]:
      cnts[x] += init_childs(ch, x)
  
  return cnts[x]

def adjust_root(x):
  global root
  
  if root == x:
    return
  
  adjust_root(parent[x])
  switch(root, x)
  root = x
  
def get_lca_c(x):
  c = 0
  
  for a in childs[x]:
    for b in childs[x]:
      if a == b:
        continue
      
      c += cnts[a] * cnts[b]
  
  c //= 2
  
  for a in childs[x]:
    c += cnts[a]
  
  return c
  
N, Q = input_n(int)
childs = [set() for _ in range(N+1)]
parent = [0]*(N+1)
adj = [[] for _ in range(N+1)]
cnts = [0]*(N+1)
initialized = [False]*(N+1)
root = 1

for _ in range(N-1):
  a, b = input_n(int)
  adj[a].append(b)
  adj[b].append(a)
  
init_childs(1, 0)
  
for _ in range(Q):
  t, x = input_n(int)
  
  if t == 1:
    adjust_root(x)
  elif t == 2:
    print(get_lca_c(x))