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
  def __init__(self):
    self.childs = []
    self.parent = -1
    self.dead = False
  def add(self, s):
    self.childs.append(s)
    s.parent = self
  def delete(self):
    self.dead = True
  def leaf_cnt(self):
    cnt = sum([c.leaf_cnt() for c in self.childs if not c.dead])
    return cnt if cnt > 0 else 1

N = input(int)
nodes = [Node() for _ in range(N)]
root = None
for i, a in enumerate(input_n(int)):
  if a == -1: root = nodes[i]
  else: nodes[a].add(nodes[i])

b = input(int)
if nodes[b].parent == -1:
  print(0)
else:
  nodes[b].delete()
  print(root.leaf_cnt())