import sys
from collections import defaultdict
sys.setrecursionlimit(1000000)

def input(_type=str):
  return _type(sys.stdin.readline().strip())
def input_n(_type=str):
  return list(map(_type, input().split()))

class SccNode:
  def __init__(self, scc, money: int, has_rest: bool, idx: int):
    self.scc = scc
    self.money = money
    self.has_rest = has_rest
    self.idx = idx
    
  def __hash__(self) -> int:
    return self.idx
  
  def __repr__(self) -> str:
    return str(self.scc)

def find_scc(graph, N, S):
  labels = [None]*N
  label_counter = 1
  
  finshed = [False]*N
  stack = []
  sccs = []
  
  def scc(end):
    scc = []
    
    while True:
      x = stack.pop()
      finshed[x] = True
      scc.append(x)
      
      if x == end:
        break
    return scc
  
  def dfs(x):
    nonlocal label_counter
    labels[x] = label_counter
    label_counter += 1
    
    parent = labels[x]
    stack.append(x)
    
    for nxt in graph[x]:
      if not labels[nxt]:
        parent = min(parent, dfs(nxt))
      elif not finshed[nxt]:
        parent = min(parent, labels[nxt])
        
    if labels[x] == parent:
      sccs.append(scc(x))
    
    return parent

  dfs(S)
  
  return sccs

def scc_nodes(sccs, moneys, is_rest):
  '''scc배열을 scc노드 객체로 변환'''
  nodes = []
  
  for idx, scc in enumerate(sccs):
    has_rest = False
    money = 0
    for x in scc:
      money += moneys[x]
      has_rest = has_rest or is_rest[x]
      
    nodes.append(SccNode(scc, money, has_rest, idx))
  
  return nodes

def node_graph(nodes, graph, N):
  '''노드 리스트를 그래프로 변환'''
  x2node = [None]*N
  for node in nodes:
    for x in node.scc:
      x2node[x] = node
  
  node_graph = defaultdict(set)
  for x in range(N):
    for nxt in graph[x]:
      x_node = x2node[x]
      nxt_node = x2node[nxt]
      
      if x_node == nxt_node or x_node == None or nxt_node == None:
        continue
      
      node_graph[x_node].add(nxt_node)
      
  return node_graph

def get_max_money(nodes:list[SccNode], node_graph: dict):
  def get_indegrees():
    indegrees = {node: 0 for node in nodes}
    
    for __from_node__, to_nodes in node_graph.items():
      for to_node in to_nodes:
        indegrees[to_node] += 1
      
    return indegrees
  
  moneys = defaultdict(lambda: 0)
  indegrees = get_indegrees()

  stack = []
  # init stack (put indegree 0)
  for node, indegree in indegrees.items():
    if indegree == 0:
      stack.append(node)
      moneys[node] = node.money
      
  while stack:
    # 기준 노드
    node = stack.pop()
    
    for nxt in node_graph[node]:
      indegrees[nxt] -= 1
      moneys[nxt] = max(moneys[nxt], moneys[node]+nxt.money)
        
      if indegrees[nxt] == 0:
        stack.append(nxt)

  return max([money for node, money in moneys.items() if node.has_rest])

N, M = input_n(int)

graph = defaultdict(list)

for _ in range(M):
  _a, _b = input_n(int)
  a = _a-1
  b = _b-1
  
  graph[a].append(b)

moneys = [input(int) for _ in range(N)]
_S, P = input_n(int)
S = _S - 1

is_rest = [False]*N
for _x in input_n(int):
  is_rest[_x-1] = True

sccs = find_scc(graph, N, S)

nodes = scc_nodes(sccs, moneys, is_rest)
n_graph = node_graph(nodes, graph, N)
max_money = get_max_money(nodes, n_graph)
print(max_money)
