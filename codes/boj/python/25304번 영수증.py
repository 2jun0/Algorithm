import sys
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

X = input(int)
N = input(int)

sum = 0
for _ in range(N):
  a, b = input_n(int)
  sum += a*b

print('Yes' if sum == X else 'No')