import sys
from collections import defaultdict
sys.setrecursionlimit(1000000)

def input(_type=str):
  return _type(sys.stdin.readline().strip())
def input_n(_type=str):
  return list(map(_type, input().split()))

def find_sccs(graph, N):
  labels = [None]*N
  label_counter = 0
  sccs = [None]*N
  scc_counter = 0
  
  stack = []
  
  def scc(end):
    nonlocal scc_counter
    
    while True:
      x = stack.pop()
      sccs[x] = scc_counter
      
      if x == end:
        break
    
    scc_counter += 1
    
  def dfs(x):
    nonlocal label_counter
    labels[x] = label_counter
    label_counter += 1
    p = labels[x]
    
    stack.append(x)
    
    for nxt in graph[x]:
      if labels[nxt] == None:
        p = min(p, dfs(nxt))
      elif sccs[nxt] == None:
        p = min(p, labels[nxt])
    
    if p == labels[x]:
      scc(x)
    return p
  
  for x in range(N):
    if not labels[x]:
      dfs(x)
      
  return sccs

def get_indegrees(sccs, graph, N):
  indegrees = [0] * (max(sccs)+1)
  
  for x in range(N):
    for nxt in graph[x]:
      if sccs[x] == sccs[nxt]:
        continue
      
      indegrees[sccs[nxt]]+=1
      
  return indegrees

T = input(int)
for t in range(T):
  N, M = input_n(int)
  
  graph = defaultdict(list)
  
  for _ in range(M):
    a, b = input_n(int)
    
    graph[a].append(b)
    
  sccs = find_sccs(graph, N)
  indegrees = get_indegrees(sccs, graph, N)
  
  if indegrees.count(0) == 1:
    for x in range(N):
      if indegrees[sccs[x]] == 0:
        print(x)
  else:
    print('Confused')
  
  if t < T-1:
    input()
    print()