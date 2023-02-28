import sys
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

N, M = input_n(int)
baskets = [0]*(N+1)
for _ in range(M):
  a, b, c = input_n(int)
  for x in range(a, b+1):
    baskets[x] = c

print(*baskets[1:])