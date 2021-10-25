import sys
INF = 10**10
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))
def print_n(L, join_str=' '):
  for i,l in enumerate(L): print(l, end=join_str if i<len(L)-1 else '\n')
def LL(n,m,d=0): return [[d]*n for _ in range(m)]
def avg(l): return sum(l)/len(l)

G = input(int)
P = input(int)
A = [input(int) for _ in range(P)]

class UnionFind:
  def __init__(self, idx):
    self.idx = idx
    self.parent = self
  def find(self):
    if self.parent != self:
      self.parent = self.parent.find()
    return self.parent
  def union(self, n):
    n.find().parent = self.find()

gates = [UnionFind(i) for i in range(G+1)]
cnt = 0
for a in A:
  n = gates[a].find()
  if n.idx == 0: break
  gates[n.idx-1].union(n)
  cnt += 1

print(cnt)