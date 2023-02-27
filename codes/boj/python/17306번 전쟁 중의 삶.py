import sys
from math import log2

def input(type=str):
  return type(sys.stdin.readline().strip())
def input_n(type=str):
  return list(map(type, input().split()))

def get_depth(x):
  dep = 0
  while x > 1:
    x //= 2
    dep += 1
  return dep

def find_lca(A):
  A_with_depth = [(get_depth(a), a) for a in A]
  A_with_depth.sort()
  
  dangers = set(A)
  
  # adjust depth to minimum
  target_dep = A_with_depth[0][0]
  nodes = set()
  for dep, a in A_with_depth:
    diff = dep - target_dep
    for _ in range(diff):
      a //= 2
      dangers.add(a)
    
    nodes.add(a)

  while len(nodes) > 1:
    nxt = set()
    for x in nodes:
      x //= 2
      dangers.add(x)
      nxt.add(x)

    nodes = nxt

  return len(dangers)
  
N = input(int)
A = input_n(int)
print(find_lca(A))