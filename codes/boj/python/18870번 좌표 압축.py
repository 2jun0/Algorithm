import sys

INF = 10**8
def input(_type=str):
	return _type(sys.stdin.readline().rstrip())
def input_n(_type=str):
	return list(map(_type, input().split()))

class Pointer:
  def __init__(self, x, idx):
    self.x = x
    self.idx = idx
  def __lt__(self, other):
    return self.x < other.x

N = input(int)
X = input_n(int)
P = [Pointer(x, i) for i, x in enumerate(X)]
P.sort()
X_ = [0]*N
i = 0
pre_p = None
for p in P:
  if pre_p and pre_p.x == p.x: 
    X_[p.idx] = X_[pre_p.idx]
  else: 
    X_[p.idx] = i
    i += 1
  pre_p = p

for x_ in X_[:-1]:
  print(x_, end=' ')
print(X_[-1])