import sys
from math import gcd

def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

T = input(int)
for _ in range(T):
  N = input(int)
  A = input_n(int)

  # a1 = d * q1 + r
  # a2 = d * q2 + r
  # a3 = d * q3 + r

  # a2 - a1 = d * (q2 - q1)
  # a3 - a2 = d * (q3 - q2)

  # d = gcd(a2 - a1, a3 - a2)의 약수 (d != 1)

  diffs = []
  for i in range(N-1):
    diffs.append(abs(A[i] - A[i+1]))

  biggest_d = gcd(*diffs)
  if biggest_d == 0:
    print('INFINITY')
  else:
    print(biggest_d)