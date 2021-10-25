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

class Matrix():
  def __init__(self, width, height, values=None, default=0):
    self.width = width
    self.height = height
    if values: self.values = values
    else: self.values = [[default]*width for _ in range(height)]
  def __mul__(self, other):
    assert other.width == self.height and other.height == self.width
    m = Matrix(other.width, self.height)
    for y in range(self.height):
      for x in range(other.width):
        for i in range(self.width):
          m.values[y][x] += self.values[y][i] * other.values[i][x]
    return m
  def __mod__(self, val):
    m = Matrix(self.width, self.height)
    for y in range(self.height):
      for x in range(self.width):
        m.values[y][x] = self.values[y][x] % val
    return m

graph = [
  [1,2],
  [0,2,3],
  [0,1,3,4],
  [1,2,4,5],
  [2,3,5,6],
  [3,4,7],
  [4,7],
  [5,6]]

m_graph = Matrix(8, 8, [
  [0,1,1,0,0,0,0,0],
  [1,0,1,1,0,0,0,0],
  [1,1,0,1,1,0,0,0],
  [0,1,1,0,1,1,0,0],
  [0,0,1,1,0,1,1,0],
  [0,0,0,1,1,0,0,1],
  [0,0,0,0,1,0,0,1],
  [0,0,0,0,0,1,1,0]
])

D = input(int)

m_cnt_pow2 = [None]*31
m_cnt_pow2[0] = m_graph
for i in range(0, 30):
  m_cnt_pow2[i+1] = (m_cnt_pow2[i]*m_cnt_pow2[i])%1000000007

m_cnt = Matrix(8,8,[
  [1,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0]
])

for i in range(30, -1, -1):
  val_pow2 = 2**i
  while val_pow2 <= D:
    m_cnt = (m_cnt * m_cnt_pow2[i])%1000000007
    D-=val_pow2
print(m_cnt.values[0][0])

