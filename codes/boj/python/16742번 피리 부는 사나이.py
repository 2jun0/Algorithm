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
  def __init__(self,i,j):
    self.p = self
    self.i = i
    self.j = j
  def find(self):
    if self.p != self:
      self.p = self.p.find()
    return self.p
  def union(self, n):
    n.find().p = self.find()

N, M = input_n(int)
table = [input() for _ in range(N)]
A = [[UnionFindNode(n,m) for m in range(M)] for n in range(N)]
for i in range(N):
  for j in range(M):
    if table[i][j] == 'U': A[i-1][j].union(A[i][j])
    elif table[i][j] == 'D': A[i+1][j].union(A[i][j])
    elif table[i][j] == 'L': A[i][j-1].union(A[i][j])
    elif table[i][j] == 'R': A[i][j+1].union(A[i][j])

visited = [[False]*M for _ in range(N)]
cnt = 0
for i in range(N):
  for j in range(M):
    p = A[i][j].find()
    if not visited[p.i][p.j]:
      visited[p.i][p.j] = True
      cnt += 1

print(cnt)
    