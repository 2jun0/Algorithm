import sys

def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

N = input(int)
A = [input(int) for _ in range(N)]

A.sort(reverse=True)
max_w = 0
cnt = 0

for a in A:
  cnt += 1
  max_w = max(max_w, a*cnt)
print(max_w)
