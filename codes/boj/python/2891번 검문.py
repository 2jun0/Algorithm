import sys
from math import gcd

def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

N = input(int)
A = [input(int) for _ in range(N)]

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
divisors = []
for i in range(1, int(biggest_d**.5) + 1):
  if biggest_d % i == 0:
    divisors.append(i)
    if i != biggest_d // i:
      divisors.append(biggest_d // i)
    
divisors.sort()
print(*divisors[1:])