import sys
from collections import defaultdict
sys.setrecursionlimit(100000)

def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

def find_sccs(graph: dict, N):
  labels = defaultdict(lambda: None)
  label_counter = 1
  finished = defaultdict(lambda: False)
  stack = []
  sccs = {}
  
  def get_scc(end):
    while True:
      x = stack.pop()
      finished[x] = True
      sccs[x] = labels[end]
      
      if x == end:
        break
  
  def dfs(x):
    nonlocal label_counter
    
    labels[x] = label_counter
    label_counter += 1
    parent = labels[x]
    stack.append(x)
    
    for nxt in graph[x]:
      if not labels[nxt]: # 방문하지 않은 경우 -> 다음 노드로
        parent = min(parent, dfs(nxt))
      elif not finished[nxt]: # 끝나지 않은 경우 -> cycle에 편입
        parent = min(parent, labels[nxt])
    
    # 탐색이 끝난경우, 자신이 지금 트리의 부모라면
    if parent == labels[x]:
      get_scc(x)
    
    return parent
  
  for x in range(1,N+1):
    for rx in [x, -x]:
      if not labels[rx]:
        dfs(rx)
  
  return sccs

def check(sccs):
  '''-x, x가 같은 사이클에 있는 지 확인'''
  for x in range(1,N+1):
    if sccs[x] == sccs[-x]:
      return False
  return True

N, M = input_n(int)
graph = defaultdict(list)

for _ in range(M):
  a, b = input_n(int)
  graph[-a].append(b)
  graph[-b].append(a)

sccs = find_sccs(graph, N)

if check(sccs):
  print(1)
else:
  print(0)
