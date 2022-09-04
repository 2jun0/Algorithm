import sys
sys.setrecursionlimit(10000000) # 재귀 제한 풀기
INF = 10**8
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))
def print_n(L, join_str=' '):
  for i,l in enumerate(L): print(l, end=join_str if i<len(L)-1 else '\n')

n, m = input(int), input(int)

costs = [[INF]*(n+1) for _ in range(n+1)]
for i in range(1,n+1): costs[i][i] = 0
for _ in range(m):
  a,b,c = input_n(int)
  costs[a][b] = min(costs[a][b],c)

for c in range(1, n+1):
  for a in range(1, n+1):
    for b in range(1, n+1):
      costs[a][b] = min(costs[a][b], costs[a][c]+costs[c][b])
for a in range(1, n+1):
  for b in range(1, n+1):
    if costs[a][b] == INF: costs[a][b] = 0
for a in range(1, n+1):
  L = [costs[a][b] for b in range(1, n+1)]
  print_n(L)