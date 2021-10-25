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

class Matrix:
  def __init__(self, v):
    self.v = v
    self.y = len(self.v)
    self.x = len(self.v[0])
  def __mul__(self, m):
    new_m = Matrix([[0]*m.x for _ in range(self.y)])
    for y in range(self.y):
      for x in range(m.x):
        for i in range(self.x):
          new_m.v[y][x] = (new_m.v[y][x] + self.v[y][i] * m.v[i][x]) % 1000003
    return new_m

MAX_a = 5
N, S, E, T = input_n(int)

def loose_matrix(M):
  new_m = Matrix([[0]*(MAX_a*M.x) for _ in range(MAX_a*M.y)])
  for y in range(M.y):
    for x in range(M.x):
      # Is self
      if y==x:
        for i in range(1, MAX_a): new_m.v[y*MAX_a+i][x*MAX_a+i-1] = 1

      if M.v[y][x] > 0:
        new_m.v[y*MAX_a][x*MAX_a+M.v[y][x]-1] = 1
    
  return new_m

A = Matrix([list(map(int, input())) for _ in range(N)])
A = loose_matrix(A)

A2X = [A]
for _ in range(30):
  A2X.append(A2X[-1]*A2X[-1])

M = Matrix([[0]*(MAX_a*N) for _ in range(MAX_a*N)])
for i in range(M.y): M.v[i][i] = 1

for i in range(len(A2X)-1, -1, -1):
  while T >= 2**i:
    T -= 2**i
    M = M*A2X[i]


print(M.v[MAX_a*(S-1)][MAX_a*(E-1)])