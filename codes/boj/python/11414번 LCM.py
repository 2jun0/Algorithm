import sys
from math import gcd

def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

def get_divisor(num):
  divisors = []
  for i in range(1, int(num**.5)+1):
    if num % i == 0:
      divisors.append(i)
      if num // i != i:
        divisors.append(num // i)
  return divisors

A, B = input_n(int)

# 1.
# A = a*D
# B = b*D
# A - B = (a-b) * D

# ->
# gcd(A+N, B+N) = gcd(A+N, abs(B-A))

# lcm(A+N, B+N) = (A+N)*(B+N) / gcd(A+N, B+N)
# lcm(A+N, B+N) = (A+N)*(B+N) / gcd(A+N, B-A)
# gcd(A+N, B-A)는 B-A의 약수 중 하나.

if A == B:
  print(1)
else:
  A, B = min(A, B), max(A, B)
  min_lcm = 10**20
  N = -1
  for divisor in get_divisor(B-A):
    n = divisor - (A % divisor)
    lcm = (A+n) * (B+n) // divisor
    if min_lcm > lcm:
      min_lcm = lcm
      N = n
  print(N)