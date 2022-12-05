import sys
from math import gcd

def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

def can_reach(p, nums):
  return p % gcd(*nums) == 0

N = input(int)

for _ in range(N):
  x, y = input_n(int)

  _K = input_n(int)
  K = _K[1:]
  if can_reach(x, K) and can_reach(y, K):
    print('Ta-da')
  else:
    print('Gave up')