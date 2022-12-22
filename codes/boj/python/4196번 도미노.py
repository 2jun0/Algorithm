import sys
from collections import defaultdict, deque
sys.setrecursionlimit(1000000)

def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

def find_sccs(graph, N):
  labels = [None]*(N+1)
  label_counter = 1
  
  sccs = [None]*(N+1)
  scc_counter = 1
  
  stack = []
  
  def scc(end):    
    while True:
      x = stack.pop()
      sccs[x] = scc_counter
      if x == end:
        break
  
  def dfs(x):
    nonlocal label_counter, scc_counter
    labels[x] = label_counter
    label_counter += 1
    parent = labels[x]
    
    stack.append(x)
    
    for nxt in graph[x]:
      if not labels[nxt]:
        parent = min(parent, dfs(nxt))
      elif not sccs[nxt]:
        parent = min(parent, labels[nxt])
        
    if parent == labels[x]:
      scc(x)
      scc_counter+=1
    
    return parent
  
  for x in range(1, N+1):
    if not labels[x]:
      dfs(x)
    
  return sccs

def group_cnt(sccs, graph, N):
  '''scc끼리 묶인 그룹의 수를 구함.'''
  indegree = [0]*(max(sccs[1:])+1)
  
  for x in range(1, N+1):
    for nxt in graph[x]:
      if sccs[x] != sccs[nxt]:
        indegree[sccs[nxt]] += 1
  return indegree.count(0) - 1

T = input(int)
for _ in range(T):
  N, M = input_n(int)
  
  graph = defaultdict(list)
  
  for _ in range(M):
    a, b = input_n(int)
    graph[a].append(b)
  
  sccs = find_sccs(graph, N)
  print(group_cnt(sccs, graph, N))