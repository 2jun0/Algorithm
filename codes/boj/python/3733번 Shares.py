import sys

def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

lines = sys.stdin.readlines()
for line in lines:
  N, S = list(map(int, line.split()))
  
  print(S // (N+1))