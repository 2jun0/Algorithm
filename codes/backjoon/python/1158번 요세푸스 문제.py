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

N, K = input_n(int)
A = [x for x in range(1,N+1)]
B = []
i = K-1
while len(A) > 0:
  i = i%len(A)
  x = A.pop(i)
  B.append(x)
  i = i+K-1
  
print('<',end='')
print_n(B, ', ', '>\n')