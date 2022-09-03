import sys
def input(_type=str):
  	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

while True:
  a, b = input_n(int)
  if a == 0 and b == 0:
    break

  print('Yes' if a > b else 'No')