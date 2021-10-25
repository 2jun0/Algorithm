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
def getLRUD(i,j): return [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]

class UnionFindNode:
  def __init__(self):
    self.p = self
    self.cnt = 1
  def union(self, node):
    if self.find() == node.find():
      return
    self.p.cnt += node.p.cnt
    node.p.p = self.p
  def find(self):
    if self.p != self: self.p = self.p.find()
    return self.p

T = input(int)
for _ in range(T):
  F = input(int)

  A_dict = {}

  for f in range(F):
    x_name, y_name = input_n(str)
    for name in [x_name, y_name]:
      if name not in A_dict.keys():
        A_dict[name] = UnionFindNode()

    A_dict[x_name].union(A_dict[y_name])
    print(A_dict[x_name].find().cnt)
