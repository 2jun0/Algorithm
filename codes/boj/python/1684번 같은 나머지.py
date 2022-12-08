import sys
from math import gcd

def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

n = input(int)
A = input_n(int)

diffs = []
for i in range(n-1):
  diffs.append(A[i+1] - A[i])
    
D = gcd(*diffs)
print(D)