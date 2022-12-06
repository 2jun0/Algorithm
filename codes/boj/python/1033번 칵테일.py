import sys
from math import gcd

def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

# 2:5 = a:b
# 3:2 = a:c

def lcm(a, b):
  return a*b // gcd(a,b)

class Edge:
  def __init__(self, from_idx, to_idx, x, y):
    self.from_idx = from_idx
    self.to_idx = to_idx
    self.x = x
    self.y = y
  
  def switch(self):
    self.from_idx, self.to_idx = self.to_idx, self.from_idx
    self.x, self.y = self.y, self.x
    
  def update(self, edge):
    if self.from_idx == edge.to_idx or self.to_idx == edge.from_idx:
      self.switch()
    
    if self.to_idx == edge.to_idx:
      self.switch()
      edge.switch()
    
    if self.from_idx == edge.from_idx:
      lcm_x = lcm(self.x, edge.x)
      self.y *= lcm_x // self.x
      edge.y *= lcm_x // edge.x
      self.x, edge.x = lcm_x, lcm_x

N = input(int)

edges = []

for _ in range(N-1):
  a, b, x, y = input_n(int)
  
  edge = Edge(a, b, x, y)
  
  edges.append(edge)
  
  # print('---')
  # for e in edges:
  #   print(e.from_idx, e.to_idx, e.x, e.y)
  # print('---')

for _ in range(N):
  for e1 in edges:
    for e in edges:
      if e1 != e:
        e.update(e1)

ratios = [0]*N
for e in edges:
  ratios[e.from_idx] = e.x
  ratios[e.to_idx] = e.y
  # print(e.from_idx, e.to_idx, e.x, e.y)

gcd_v = gcd(*ratios)
for i, x in enumerate(ratios):
  ratios[i] = x//gcd_v
  
print(*ratios)