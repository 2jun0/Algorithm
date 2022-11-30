import sys

def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

N = input(int)
M = input(int)
A = set(input_n(int))

cnt = 0
for a in A:
  if a*2 != M and M-a in A:
    cnt += 1
    
print(cnt//2)