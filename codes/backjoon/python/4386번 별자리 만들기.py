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
def avg(l): return sum(l)/len(l)


class UnionFindNode:
  def __init__(self):
    self.parent = self
  def union(self, node):
    node.find().parent = self.find()
  def find(self):
    if self.parent != self:
      self.parent = self.parent.find()
    return self.parent

n = input(int)

A = [input_n(float) for _ in range(n)]
nodes = [UnionFindNode() for _ in range(n)]

L = []
for a in range(n):
  for b in range(a, n):
    l = ((A[a][0]-A[b][0])**2 + (A[a][1]-A[b][1])**2)**.5
    L.append((l, a, b))
L.sort()

sum_v = 0
for l, a, b in L:
  if nodes[a].find() != nodes[b].find():
    nodes[a].union(nodes[b])
    sum_v += l
print(sum_v)