import sys

def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

A = [input(int) for _ in range(9)]

from itertools import combinations

for B in combinations(A, 7):
  if sum(B) == 100:
    for b in sorted(B):
      print(b)
    break