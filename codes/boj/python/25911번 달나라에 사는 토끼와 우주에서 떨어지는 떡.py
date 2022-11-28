import sys

def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

################
# 다시 풀어야 함...
################

def come_from(x, srt, visited, d):
  if visited[x]:
    return
  visited[x] = True
  dists[srt][x] = d

  rabbits_list[x].move(d)
  rabbits_list[srt].merge(rabbits_list[x])

  for prev in prevs[x]:
    come_from(prev, srt, visited, d+dists[prev][x])

class Rabbit:
  def __init__(self, idx, r):
    self.idx = idx
    self.a = 0
    self.r = r
    self.pos = idx

  def move(self, dst, d):
    self.a += d*self.r
    self.pos = dst

class Rabbits:
  def __init__(self, rabbits, pos):
    self._rabbits = rabbits
    self.lazy_d = 0
    self.pos = pos

  def merge(self, other):
    if self == other:
      return

    _ = self.get_rabbits()
    other_rabbits = other.get_rabbits()
    self._rabbits.extend(other_rabbits)

    other._rabbits = []

  def move(self, d):
    self.lazy_d += d

  def get_rabbits(self):
    if self.lazy_d > 0:
      for rabbit in self._rabbits:
        rabbit.move(self.pos, self.lazy_d)
      self.lazy_d = 0
    return self._rabbits

N = input(int)

dists = [[-1]*N for _ in range(N)]
prevs = [[] for _ in range(N)]
for i in range(N):
  _x, d = input_n(int)
  x = _x-1
  dists[i][i] = 0
  dists[i][x] = d
  prevs[x].append(i)

R = input_n(int)
M = input(int)
V = [_v-1 for _v in input_n(int)]

rabbits_list = [Rabbits([Rabbit(i, R[i])], i) for i in range(N)]
availalbe_rabbits_
for v in V:
  

  come_from(v, v, [False]*N, 0)

A = [0]*N
for rabbits in rabbits_list:
  for rabbit in rabbits.get_rabbits():
    A[rabbit.idx] = rabbit.a

for a in A:
  print(a)