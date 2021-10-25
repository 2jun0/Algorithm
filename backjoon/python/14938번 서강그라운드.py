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

n, m, r = input_n(int)
dists = LL(n+1, n+1, INF)
for i in range(n+1): dists[i][i] = 0
items = [0]+input_n(int)

for _ in range(r):
  a,b,l = input_n(int)
  dists[a][b] = min(dists[a][b], l)
  dists[b][a] = min(dists[b][a], l)

for c in range(n+1):
  for a in range(n+1):
    for b in range(n+1):
      dists[a][b] = min(dists[a][b],dists[a][c]+dists[c][b])

result = 0
for a in range(n+1):
  sum = 0
  for b in range(n+1):
    if dists[a][b] <= m: sum+=items[b]
  result = max(result, sum)

print(result)