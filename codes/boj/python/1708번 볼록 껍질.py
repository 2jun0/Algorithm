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
def getLRUD(i,j): return [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]

root = None

def ccw(A,B,C):
  ccw = A.x*B.y+B.x*C.y+C.x*A.y - (A.y*B.x+B.y*C.x+C.y*A.x)
  if ccw > 0: return 1
  elif ccw == 0: return 0
  else: return -1

class Vec:
  def __init__(self, x, y):
    self.y = y
    self.x = x
  def __lt__(self, v):
    if (v.x-root.x)*(self.y-root.y) != (v.y-root.y)*(self.x-root.x):
      return (v.x-root.x)*(self.y-root.y) < (v.y-root.y)*(self.x-root.x)
    if self.y != v.y:
      return self.y < v.y
    return self.x < v.x

N = input(int)
A_ = []
for _ in range(N):
  x,y = input_n(int)
  A_.append((y,x))
A_.sort()

root = Vec(A_[0][1], A_[0][0])
A = []
for y,x in A_[1:]: A.append(Vec(x,y))
A.sort()

hull = [root, A[0]]
for i in range(1, len(A)):
  while len(hull) >= 2:
    a2 = hull.pop()
    a1 = hull[-1]
    if ccw(a1,a2,A[i]) > 0:
      hull.append(a2)
      break
  hull.append(A[i])
print(len(hull))