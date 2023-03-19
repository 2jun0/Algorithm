import sys
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

N = input(int)
A = input_n(int)
v = input(int)

cnt = 0
for a in A:
  if a == v:
    cnt += 1

print(cnt)