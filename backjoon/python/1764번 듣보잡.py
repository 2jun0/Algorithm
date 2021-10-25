import sys

def input(_type=str):
	return _type(sys.stdin.readline().rstrip())
def input_n(_type):
	return list(map(_type, input().split()))

N, M = input_n(int)
A = set(input() for _ in range(N))
B = [input() for _ in range(M)]
B.sort()

C = []
for b in B:
  if b in A:
    C.append(b)

print(len(C))
for c in C:
  print(c)