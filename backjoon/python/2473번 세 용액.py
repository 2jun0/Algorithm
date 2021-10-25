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
A.sort()
min_val = INF
min_cab = (-1,-1)
for c in range(N):
  a, b = c+1, N-1
  while a < b:
    if abs(A[a] + A[b] + A[c]) < min_val:
      min_val = abs(A[a] + A[b] + A[c])
      min_cab = (A[c],A[a],A[b])
    
    if A[a] + A[b] + A[c] < 0: a+=1
    else: b-=1
print(min_cab[0], min_cab[1], min_cab[2])