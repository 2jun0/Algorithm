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

class Matrix:
  def __init__(self, arr):
    self.arr = arr
  def __mul__(self, m):
    n = Matrix([[0,0],[0,0]])
    for y in range(len(self.arr)):
      for mx in range(len(m.arr[0])):
        for i in range(len(self.arr[0])):
          n.arr[y][mx] += self.arr[y][i]*m.arr[i][mx] % 1000000007
    return n

mpow = [Matrix([[0,1],[1,1]])]

for _ in range(60):
  mpow.append(mpow[-1] * mpow[-1])

n = input(int)
result_m = Matrix([[0,1]])

for i, m in enumerate(mpow):
  re_i = len(mpow)-i-1

  while 2**re_i <= n:
    n -= 2**re_i
    result_m = result_m * mpow[re_i]
print(result_m.arr[0][0] % 1000000007)