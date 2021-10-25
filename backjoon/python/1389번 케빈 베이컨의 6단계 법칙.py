import sys

INF = 10**8
def input(_type=str):
	return _type(sys.stdin.readline().rstrip())
def input_n(_type=str):
	return list(map(_type, input().split()))
def print_n(L):
  s = ''
  for l in L: s+='{} '.format(l)
  print(s[:-1])

N, M = input_n(int)
graph = [[INF]*(N+1) for _ in range(N+1)]
for _ in range(M):
  a,b = input_n(int)
  graph[a][b] = 1
  graph[b][a] = 1
for a in range(1, N+1):
  graph[a][a] = 0 

for c in range(1, N+1):
  for a in range(1, N+1):
    for b in range(1, N+1):
      graph[a][b] = min(graph[a][b], graph[a][c] + graph[c][b])

bacons = [0]*(N+1)
for a in range(1, N+1):
  for b in range(1, N+1):
    bacons[a] += graph[a][b]

class Pointer:
  def __init__(self, x, idx):
    self.x = x
    self.idx = idx
  def __lt__(self, other):
    return (self.x, other.idx) < (other.x, other.idx)
  @classmethod
  def to_pointer_list(cls, L):
    return [Pointer(l, i) for i, l in enumerate(L)]

p_bacons = Pointer.to_pointer_list(bacons)
p_bacons.sort()
print(p_bacons[1].idx)