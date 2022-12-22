import sys
from collections import defaultdict
sys.setrecursionlimit(1000000)

lines = sys.stdin.readlines()
l_i = 0
def input(_type=str):
  global l_i
  l_i+=1
  return _type(lines[l_i-1].strip())
def input_n(_type=str):
  return list(map(_type, input().split()))

def find_sccs(graph, n):
  labels = [None]*(2*n+1)
  label_counter = 0
  finished = [False]*(2*n+1)
  stack = []
  sccs = []
  scc_idxs = [-1]*(2*n+1)
  
  def add_scc(end):
    scc = []
    while True:
      x = stack.pop()
      scc.append(x)
      finished[x] = True
      scc_idxs[x] = len(sccs)
      
      if x == end:
        break
    sccs.append(scc)
  
  def dfs(x):
    nonlocal label_counter
    
    labels[x] = label_counter
    label_counter += 1
    stack.append(x)
    p = labels[x]
    
    for nxt in graph[x]:
      if labels[nxt] == None:
        p = min(p, dfs(nxt))
      elif not finished[nxt]:
        p = min(p, labels[nxt])
    
    if p == labels[x]:
      add_scc(x)
    
    return p
    
  for x in range(1,n+1):
    if labels[n-x] == None:
      dfs(n-x)
    if labels[n+x] == None:
      dfs(n+x)
      
  return sccs, scc_idxs
      
while l_i < len(lines):
  n, m = input_n(int)
  graph = defaultdict(list)

  for _ in range(m):
    a, b = input_n(int)
    
    # a or b
    # not a -> b
    # not b -> a
    graph[n-a].append(b+n)
    graph[n-b].append(a+n)

  graph[n-1].append(n+1)
  sccs,scc_idxs = find_sccs(graph, n)

  flag = True
  # if scc_idxs[1+n] == scc_idxs[n-1]:
  #   flag = False
  
  for x in range(1, n+1):
    if scc_idxs[x+n] == scc_idxs[n-x]:
      flag = False
      break
  if flag:
    print('yes')
  else:
    print('no')