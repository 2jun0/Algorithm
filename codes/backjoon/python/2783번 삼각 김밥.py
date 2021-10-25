import sys
sys.setrecursionlimit(10000000) # 재귀 제한 풀기

def input(_type=str):
	return _type(sys.stdin.readline().rstrip())
def input_n(_type):
	return list(map(_type, input().split()))

x, y = input_n(int)
min_r = x/y
N = input(int)

for _ in range(N):
  x, y = input_n(int)
  if x/y < min_r:
    min_r = x/y 

print(min_r*1000)