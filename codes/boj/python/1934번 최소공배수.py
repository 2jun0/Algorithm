import sys
from math import gcd

def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

T = input(int)
for _ in range(T):
  A, B = input_n(int)
  print(A*B // gcd(A, B))
  