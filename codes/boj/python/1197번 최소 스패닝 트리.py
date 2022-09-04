import sys
sys.setrecursionlimit(10000000) # 재귀 제한 풀기
INF = 10**8
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))
def print_n(L, join_str=' '):
  for i,l in enumerate(L): print(l, end=join_str if i<len(L)-1 else '\n')
def LL(n,m,d=0): return [[d]*n for _ in range(m)]

class UnionFindNode:
  def __init__(self):
    self.parent = self

  def union(self, node):
    node.parent.find().parent = self.find()
  
  def find(self):
    if self.parent != self:
      self.parent = self.parent.find() # 최적화
    return self.parent

V, E = input_n(int)
h = []
for _ in range(E):
  a,b,c = input_n(int)
  h.append((c,a,b))
h.sort()

Ns = [UnionFindNode() for _ in range(V+1)]

w = 0
for c,a,b in h:
  if Ns[a].find() == Ns[b].find():
    continue
  Ns[a].union(Ns[b])
  w+=c

print(w)