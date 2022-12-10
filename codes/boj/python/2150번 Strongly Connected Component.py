import sys
from collections import defaultdict

sys.setrecursionlimit(100000)

def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

def find_SCC(graph, N):
  sccs = []
  
  label_counter = 1
  labels = [None]*(N+1)
  finished = [False]*(N+1)
  
  stack = []
  
  def get_scc(end):
    scc = []
    while True:
      x = stack.pop()
      
      finished[x] = True
      scc.append(x)
      
      if x == end:
        break
    return sorted(scc)
  
  def dfs(x):
    """get my cycle's parent"""
    nonlocal label_counter
    
    labels[x] = label_counter
    label_counter += 1
    stack.append(x)
    parent = labels[x]
    
    for nxt in graph[x]:
      if not labels[nxt]: # 새로운 노드
        parent = min(parent, dfs(nxt))
      elif not finished[nxt]: # cycle 형성 및 편입
        parent = min(parent, labels[nxt])
      
    if parent == labels[x]:
      sccs.append(get_scc(x))
    
    return parent
  
  for x in range(1, N+1):
    if not labels[x]:
      dfs(x)
  return sccs

V, E = input_n(int)
graph = defaultdict(list)

for _ in range(E):
  a, b = input_n(int)
  graph[a].append(b)
  
sccs = find_SCC(graph, V)
sccs.sort(key=lambda scc: scc[0])

print(len(sccs))
for scc in sccs:
  print(*scc, -1)