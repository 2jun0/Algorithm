import sys
from collections import deque
sys.setrecursionlimit(100000)

def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

def find_travel_cnt_by_sccs(graph, N, s, t):
  labels = [-1]*N
  label_counter = 0
  stack = []
  scc_idxs = [-1]*N
  sccs = []
  
  def get_scc(end):
    scc = []
    scc_idx = len(sccs)
    while stack:
      x = stack.pop()
      scc_idxs[x] = scc_idx
      scc.append(x)
      
      if end == x:
        break

    sccs.append(scc)
  
  def dfs(x):
    nonlocal label_counter
    
    labels[x] = label_counter
    label_counter += 1
    stack.append(x)
    p = labels[x]
    
    for nxt in graph[x]:
      if labels[nxt] == -1:
        p = min(p, dfs(nxt)) 
      elif scc_idxs[nxt] == -1:
        p = min(p, labels[nxt])
    
    if p == labels[x]:
      get_scc(x)
    
    return p
  
  dfs(s)
  
  graph_scc = [[] for _ in range(len(sccs))]
  in_scc = [0]*len(sccs)
  for x in range(N):
    for nxt in graph[x]:
      if scc_idxs[x] >= 0 and scc_idxs[nxt] >= 0 and scc_idxs[x] != scc_idxs[nxt]:
        graph_scc[scc_idxs[x]].append(scc_idxs[nxt])
        in_scc[scc_idxs[nxt]] += 1
  
  if scc_idxs[t] == -1:
    return 0
  
  # 위상정렬 시작.
  q = deque()
  q.append(scc_idxs[s])
  
  cnts = [0]*len(sccs)
  cnts[scc_idxs[s]] = len(sccs[scc_idxs[s]])
  
  while q:
    idx = q.popleft()
    
    for nxt_idx in graph_scc[idx]:
      cnts[nxt_idx] = max(cnts[nxt_idx], cnts[idx] + len(sccs[nxt_idx]))
      in_scc[nxt_idx] -= 1
      
      if in_scc[nxt_idx] == 0:
        q.append(nxt_idx)
  return cnts[scc_idxs[t]]

N, M, S, T = input_n(int)
S -= 1
T -= 1

graph = [[] for _ in range(N)]

for _ in range(M):
  a, b = input_n(int)
  a-=1
  b-=1
  graph[a].append(b)

print(find_travel_cnt_by_sccs(graph, N, S, T))
