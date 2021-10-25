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

N, M, K = input_n(int)
A = input_n(int)
B = input_n(int)

A.sort()

class UnionFindNode:
  def __init__(self, idx):
    self.p = self
    self.idx = idx
  def find(self):
    if self.p != self:
      self.p = self.p.find()
    return self.p
  def union(self,n):
    n.find().p = self.find()

AN = [UnionFindNode(i) for i in range(M)]

def bsearch(A, x):
  start, end = 0, len(A)
  while start < end:
    mid = (start+end)//2
    if A[mid]<=x:
      start = mid+1
    else:
      end = mid
  return start

for b in B:
  idx = bsearch(A, b)
  p = AN[idx].find()
  if p.idx+1 < M: AN[p.idx+1].union(AN[p.idx])
  print(A[p.idx])