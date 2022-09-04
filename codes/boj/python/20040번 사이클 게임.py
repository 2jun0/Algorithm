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
    self.p = self
  def find(self):
    if self.p != self:
      self.p = self.p.find()
    return self.p
  def union(self, n):
    n.find().p = self.find()

N, M = input_n(int)
A = [UnionFindNode() for _ in range(N)]

result = 0
for i in range(1,M+1):
  a, b = input_n(int)
  if result != 0: continue
  if A[a].find() == A[b].find(): result = i; continue
  A[a].union(A[b])

print(result)