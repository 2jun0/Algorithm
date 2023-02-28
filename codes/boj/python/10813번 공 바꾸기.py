import sys

def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

N, M = input_n(int)
A = [x for x in range(0, N+1)]
for _ in range(M):
  a, b = input_n(int)
  A[a], A[b] = A[b], A[a]
print(*A[1:])