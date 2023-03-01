import sys

def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))  

N, K = input_n(int)
xn = 1
# X[n] = (X[n-1] + K - 1) % n + 1
for n in range(2, N+1):
  xn = (xn + K - 1) % n + 1
print(xn)