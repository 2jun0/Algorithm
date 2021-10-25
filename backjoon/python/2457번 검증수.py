import sys

def input(_type=str):
	return _type(sys.stdin.readline().rstrip())
def input_n(_type):
	return list(map(_type, input().split()))

A = input_n(int)
sum = 0
for a in A:
  sum += a**2
print(sum%10)