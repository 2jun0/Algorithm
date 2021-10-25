import sys

def input(_type=str):
	return _type(sys.stdin.readline().rstrip())
def input_n(_type):
	return list(map(_type, input().split()))

N = input(int)
A = set(input_n(int))
M = input(int)
A2 = input_n(int)

for a in A2:
  if a in A:print(1)
  else:print(0)