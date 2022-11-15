import sys

def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

N = input(int)
cnts = [0]*(N+1)
cnts[0] = 1

for i in range(1,N+1):
  if 0 <= i - 2:
    cnts[i] += cnts[i-2] * 3

  for i2 in range(i - 4, -1, -2):
    cnts[i] += cnts[i2] * 2

print(cnts[-1])