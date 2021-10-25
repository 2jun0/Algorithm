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
A = input_n(int)
L = [-1]*N
for i, a in enumerate(A):
  cnt = 0
  a_i = 0
  while cnt < a:
    if L[a_i] == -1: cnt+=1
    a_i +=1
  while L[a_i] != -1: a_i+=1
  L[a_i] = i+1
print_n(L)