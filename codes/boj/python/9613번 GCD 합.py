import sys
from math import gcd
from itertools import combinations

def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

T = input(int)
for _ in range(T):
  A = input_n(int)
  A = A[1:]
  v = 0
  
  for two in combinations(A, 2):
    v += gcd(*two)
    
  print(v)