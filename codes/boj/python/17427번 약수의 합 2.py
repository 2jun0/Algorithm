import sys
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

n = input(int)
print(sum(k*(n//k) for k in range(1,n+1)))