import sys
sys.setrecursionlimit(10000000) # 재귀 제한 풀기
INF = 10**10
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))
def print_n(L, join_str=' ', end_str='\n'):
  for i,l in enumerate(L): print(l, end=join_str if i<len(L)-1 else end_str)
def LL(n,m,d=0): return [[d]*n for _ in range(m)]

A, B = input_n()
C = int(A,2) + int(B,2)
print(str(bin(C))[2:])