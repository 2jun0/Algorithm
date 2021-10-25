import sys
sys.setrecursionlimit(10000000) # 재귀 제한 풀기
INF = 10**8
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))
def print_n(L, join_str=' '):
  for i,l in enumerate(L): print(l, end=join_str if i<len(L)-1 else '\n')
def LL(n,m,d=0): return [[d]*n for _ in range(m)]

N = input(int)
W = [input_n(int) for _ in range(N)]
for i in range(N):
  for j in range(N):
    if i!=j and W[i][j] == 0:
      W[i][j] = INF
      
dists = [[INF]*(1<<N) for _ in range(N)]
def func(x, visited):
  # end
  if visited == (1<<N)-1: return W[x][0]
  if dists[x][visited] < INF: return dists[x][visited]

  for y in range(N):
    if (1 << y) & visited or W[x][y] == INF: continue
    dists[x][visited] = min(dists[x][visited], W[x][y]+func(y, visited|(1<<x)))
  return dists[x][visited]

print(func(0, 1))