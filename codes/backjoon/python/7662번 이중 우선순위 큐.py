import sys

INF = 10**8
def input(_type=str):
	return _type(sys.stdin.readline().rstrip())
def input_n(_type=str):
	return list(map(_type, input().split()))



import heapq
class DoubleHeap:
  class Node:
    def __init__(self, val):
      self.is_dead = False
      self.val = val
    def __lt__(self, other):
      return self.val < other.val

  def __init__(self):
    self.max_h = []
    self.min_h = []
    self.len = 0
  def push(self, x):
    n = self.Node(x)
    heapq.heappush(self.max_h, (-x, n))
    heapq.heappush(self.min_h, (x, n))
    self.len+=1
  def pop_max(self):
    n = self._pop(self.max_h)
    return n.val
  def pop_min(self):
    n = self._pop(self.min_h)
    return n.val
  def get_max(self):
    n = self._get_top(self.max_h)
    return n.val
  def get_min(self):
    n = self._get_top(self.min_h)
    return n.val
  def _pop(self, h):
    n = heapq.heappop(h)[1]
    while n.is_dead: n = heapq.heappop(h)[1]
    n.is_dead = True
    self.len -= 1
    return n
  def _get_top(self, h):
    while h[0][1].is_dead: heapq.heappop(h)
    return h[0][1]
  def __len__(self):
    return self.len

T = input(int)
for _ in range(T):
  N = input(int)
  h = DoubleHeap()
  for __ in range(N):
    cmd, arg = input_n()
    arg = int(arg)
    if cmd == 'I':
      h.push(arg)
    elif cmd == 'D':
      if len(h) == 0:
        continue
      if arg == 1:
        h.pop_max()
      if arg == -1:
        h.pop_min()
  if len(h) > 0: print(h.get_max(), h.get_min())
  else: print('EMPTY')