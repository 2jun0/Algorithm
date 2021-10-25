import sys
sys.setrecursionlimit(10000000) # 재귀 제한 풀기

def input(_type=str):
	return _type(sys.stdin.readline().rstrip())
def input_n(_type):
	return list(map(_type, input().split()))

n = input(int)
alist = input_n(int)
x = input(int)

table = [False] * 1000001
for a in alist:
  table[a] = True

cnt = 0
for a in alist:
  if x-a >= 1 or x-a < 1000000:
    if table[x-a]:
      cnt+=1

print(cnt//2)
