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

N, A, B = input_n(int)
A, B = min(A,B), max(A,B)
r = 1
while A<B:
  if B%2==0 and A+1==B: break
  N = (N+1)//2
  A = (A+1)//2
  B = (B+1)//2
  r+=1

print(r)
