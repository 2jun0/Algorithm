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
def avg(l): return sum(l)/len(l)

N = input(int)
A = []
for _ in range(N):
  r, c = input_n(int)
  A.append((r,c))

V = [[INF]*N for _ in range(N)]
for i in range(N): V[i][i] = 0
# a~b-1 * b~a+r
# r : 1   ~ N-1
# a : 0   ~ N-1-r
# b : a+1 ~ a+r
for r in range(1, N):
  for a in range(N-r):
    for b in range(a+1, a+r+1):
      V[a][a+r] = min(
        V[a][a+r], 
        V[a][b-1]+V[b][a+r]+A[a][0]*A[b][0]*A[a+r][1]
      )

print(V[0][-1])