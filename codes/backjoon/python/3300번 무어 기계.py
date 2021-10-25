import sys
sys.setrecursionlimit(10000000) # 재귀 제한 풀기
INF = 10**10
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))
def print_n(L, join_str=' '):
  for i,l in enumerate(L): print(l, end=join_str if i<len(L)-1 else '\n')
def LL(n,m,d=0): return [[d]*n for _ in range(m)]

class Node:
  def __init__(self, simbol):
    self.simbol = simbol
    self._simbol = None
  def __repr__(self) -> str:
    return self.simbol
  def match(self, simbol):
    if self._simbol and self._simbol == simbol: return [self._simbol]
    elif self.simbol == simbol: return [self.simbol]
    elif not self._simbol and self.simbol == '_': return [self.simbol]
    else: []
  def next(self):
    return False
  def mode2(self, _val):
    if self.simbol == '_': self._simbol = _val

class MultiNode:
  def __init__(self, *ns):
    self.nodes = []
    for n in ns:
      if isinstance(n, MultiNode): self.nodes.extend(n.nodes)
      else: self.nodes.append(n)
  def __repr__(self) -> str:
    S = '['
    for n in self.nodes[:-1]: S+=n.__repr__()+','
    S+=self.nodes[-1].__repr__()+']'
    return S
  def match(self, simbol):
    L = []
    for n in self.nodes:
      tmp = n.match(simbol)
      if tmp: L.extend(tmp)
    return L
  def next(self):
    nextable = False
    for n in self.nodes: nextable |= n.next()
    return nextable
  def mode2(self, _val):
    for n in self.nodes: n.mode2(_val)

class NextNode:
  def __init__(self, *ns):
    self.nodes = []
    self.pointer = 0
    for n in ns:
      if isinstance(n, NextNode): self.nodes.extend(n.nodes)
      else: self.nodes.append(n)
  def __repr__(self):
    S = ''
    for n in self.nodes[:-1]: S+=n.__repr__()+'->'
    S+=self.nodes[-1].__repr__()
    return S
  def match(self, simbol):
    if self.pointer < len(self.nodes):
      L = self.nodes[self.pointer].match(simbol)
      if not L: self.pointer = INF
      return L
    else:
      return []
  def next(self):
    if self.pointer >= len(self.nodes): return False
    nextable = self.nodes[self.pointer].next()
    if not nextable:
      self.pointer+=1
    return self.pointer < len(self.nodes)
  def mode2(self, _val):
    self.pointer = 0
    for n in self.nodes: n.mode2(_val)

def nodize(pattern):
  nodes = []
  s = []
  i = 0
  while i < len(pattern):
    p = pattern[i]
    if p == '|': s.append(p)
    elif p == '(': 
      if i>0 and pattern[i-1] not in ['(', '|']:
        s.append('>')
      s.append(p)
    elif p == ')':
      while s[-1] != '(':
        cmd = s.pop()
        if cmd == '|':
          B = nodes.pop()
          A = nodes.pop()
          nodes.append(MultiNode(A,B))
      s.pop()
    else:
      nodes.append(Node(p))
      if i>0 and pattern[i-1] not in ['(', '|']:
        s.append('>')
    
    while len(s) > 0 and s[-1] == '>':
      s.pop()
      B = nodes.pop()
      A = nodes.pop()
      nodes.append(NextNode(A,B))
        
    i+=1
  return nodes[-1]

def check(L, node):
  _simbol = []
  flag_valid = True
  for i, l in enumerate(L):
    simbols = node.match(l)
    if not simbols: 
      flag_valid = False
      break
    if '_' in simbols:
      _simbol.append(l)
    nextable = node.next()
    if i<len(L)-1 and not nextable: 
      flag_valid = False
      break
  if node.next(): flag_valid = False
  return (flag_valid, set(_simbol))

T = input(int)

for _ in range(T):
  pattern = '('+input()+')'
  node = nodize(pattern)
  L = input()
  flag_valid, simbols = check(L, node)
  if not flag_valid:
    print('!')
    continue

  cnt, _ = 0, ''
  for s in simbols:
    node.mode2(s)
    flag_valid, simbols = check(L, node)
    if flag_valid: cnt+=1; _ = s
  node.mode2('@')
  flag_valid, simbols = check(L, node)

  if cnt > 1 or cnt == 0 or flag_valid:
    print('_')
  else: 
    print(_)