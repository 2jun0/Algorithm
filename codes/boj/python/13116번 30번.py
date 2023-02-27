import sys

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

def lca(a, b):
  a_dep = get_depth(a)
  b_dep = get_depth(b)
  if a_dep > b_dep:
    a, b = b, a
    a_dep, b_dep = b_dep, a_dep
  
  diff = b_dep - a_dep
  for _ in range(diff):
    b //= 2
  
  while a != b:
    a //= 2
    b //= 2
  
  return a

T = input(int)
for _ in range(T):
  a,b = input_n(int)
  print(10 * lca(a, b))