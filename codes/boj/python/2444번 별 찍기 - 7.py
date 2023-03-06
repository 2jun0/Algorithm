import sys

def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

N = input(int)
for i in range(1,N+1):
  print(' '*(N-i) + '*'*(2*i-1))
for i in range(N-1,0,-1):
  print(' '*(N-i) + '*'*(2*i-1))