import sys
sys.setrecursionlimit(10000000) # 재귀 제한 풀기
INF = 10**10
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))
def print_n(L, join_str=' '):
  for i,l in enumerate(L): print(l, end=join_str if i<len(L)-1 else '\n')
def LL(n,m,d=0): return [[d]*n for _ in range(m)]

N = input(int)
table = [[0]*100 for _ in range(100)]
for _ in range(N):
  a,b = input_n(int)
  for ta in range(a,a+10):
    for tb in range(b,b+10):
      table[ta][tb] = 1
print(sum([sum(t) for t in table]))
