import sys
sys.setrecursionlimit(10000000) # 재귀 제한 풀기

def input(_type=str):
	return _type(sys.stdin.readline().rstrip())
def input_n(_type):
	return list(map(_type, input().split()))

T = input(int)
for _ in range(T):
  pos, st = input_n(str)
  pos = int(pos)

  print(st[:pos-1] + st[pos:])