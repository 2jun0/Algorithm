import sys
from collections import deque
def input(_type=str):
  return _type(sys.stdin.readline().strip())
def input_n(_type=str):
  return list(map(_type, input().split()))

def parse(s):
  all = [[]]
  C = s.split()
  i = 0
  while i < len(C):
    while not C[i]:
      i+=1
    a = int(C[i])
    i+=1
    while not C[i]:
      i+=1
    b = int(C[i])
    i+=1
    if a == 0 and b == 0:
      all.append([])
    elif a == -1 and b == -1:
      break
    else:
      all[-1].append((a,b))
    
  return all[:-1]

def input_all():
  all = ''
  while True:
    s = input()
    all += ' ' + s
    
    if s.endswith('-1'):
      break
  return all

def bfs(adjs: dict, root):
  visited = {x : False for x in adjs.keys()}
  q = deque()
  
  visited[root] = True
  q.append(root)
  
  while q:
    x = q.popleft()
    
    for n in adjs[x]:
      # multiple route
      if visited[n]:  
        return False
      visited[n] = True
      q.append(n)
  
  # can't visit all nodes
  for v in visited.values():
    if v == False:
      return False
    
  return True

alls = input_all()
all = parse(alls)
for t in range(len(all)):
  A = all[t]
  is_tree=True
  
  # zero node is a tree
  if not A:
    print(f'Case {t+1} is a tree.')
    continue
  
  adjs = {}
  indegrees = {}
  for a, b in A:
    indegrees.setdefault(a, 0)
    indegrees.setdefault(b, 0)
    
    adjs.setdefault(a, [])
    adjs.setdefault(b, [])
    
    # self to self route
    if a == b:
      is_tree = False
  for a, b in A:
    adjs[a].append(b)
    indegrees[b] += 1
  
  root = None
  for x, indegree in indegrees.items():
    if indegree == 0:
      # multiple roots
      if root != None:
        is_tree = False
      
      root = x
    elif indegree > 1:
      # multiple indegrees
      is_tree = False
  
  # no root
  if root == None:
    is_tree = False
  is_tree = is_tree and bfs(adjs, root)
  if is_tree:
    print(f'Case {t+1} is a tree.')
  else:
    print(f'Case {t+1} is not a tree.')