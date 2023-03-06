import sys

def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

N, M = input_n(int)
A = [x for x in range(N+1)]
for _ in range(M):
  a, b = input_n(int)
  diff = b-a
  idx = 0
  while a + idx < b - idx:
    A[b - idx], A[a + idx] = A[a + idx], A[b - idx]
    idx+=1
    
print(*A[1:])