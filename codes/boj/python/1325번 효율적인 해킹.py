import sys
from collections import deque
sys.setrecursionlimit(10000)
def input(_type=str):
  return _type(sys.stdin.readline().strip())
def input_n(_type=str):
  return list(map(_type, input().split()))

N, M = input_n(int)
graph = [[] for _ in range(N)]
for _ in range(M):
  _a, _b = input_n(int)
  graph[_b-1].append(_a-1)

def find_scc(graph):
  sccs = []
  labels = [None]*N
  label_counter = 1
  finished = [False]*N
  s = []
  
  def get_scc(end):
    scc = []
    while s:
      x = s.pop()
      finished[x] = True
      scc.append(x)
      if x == end:
        break
    return scc
  
  def dfs(x):
    nonlocal label_counter
    
    labels[x] = label_counter
    label_counter+=1
    s.append(x)
    p = labels[x]
    
    for nxt in graph[x]:
      if labels[nxt] == None:
        p = min(p, dfs(nxt))
      elif not finished[nxt]:
        p = min(p, labels[nxt])
    
    if p == labels[x]:
      sccs.append(get_scc(x))
    
    return p
      
  for x in range(N):
    if labels[x] == None:
      dfs(x)
      
  return sccs

def get_scc_graph(sccs, graph):
  scc_graph = [set() for _ in range(len(sccs))]
  indegrees = [0]*len(sccs)
  x2scc_idx = [0]*N
  for idx in range(len(sccs)):
    for x in sccs[idx]:
      x2scc_idx[x] = idx
  
  for x in range(N):
    for nxt in graph[x]:
      x_idx = x2scc_idx[x]
      nxt_idx = x2scc_idx[nxt]
      if x_idx == nxt_idx:
        continue
      indegrees[nxt_idx] += 1
      scc_graph[x_idx].add(nxt_idx)
      
  return scc_graph, indegrees

def get_cnt_bfs(s):
  q = deque()
  visited = [False]*len(sccs)
  
  q.append(s)
  visited[s] = True
  cnt = 0
  
  while q:
    idx = q.popleft()
    cnt += len(sccs[idx])
    
    for nxt in scc_graph[idx]:
      if not visited[nxt]:
        visited[nxt] = True
        q.append(nxt)

  return cnt

sccs = find_scc(graph)
scc_graph, indegrees = get_scc_graph(sccs, graph)
m = 0
ans = []
for idx in range(len(sccs)):
  if indegrees[idx] == 0:
    cnt = get_cnt_bfs(idx)
    if m < cnt:
      m = cnt
      ans.clear()
      
    if m == cnt:
      for x in sccs[idx]:
        ans.append(x+1)

ans.sort()
print(*ans)