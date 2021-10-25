import sys
sys.setrecursionlimit(10000000) # 재귀 제한 풀기
INF = 10**8
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))
def print_n(L, join_str=' '):
  s = ''
  for l in L[:-1]: s+='{}{}'.format(l, join_str)
  s+='{}'.format(L[-1])
  print(s)

n = input(int)
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
  a,b,d = input_n(int)
  graph[a].append((b,d))
  graph[b].append((a,d))

visited = [False]*(n+1)
def dfs(x):
  if visited[x]: return (-1, -1)
  visited[x] = True

  max_i, max_d = x, 0
  for y, d in graph[x]:
    yy, yd = dfs(y)
    if yy == -1: continue
    if max_d < yd+d:
      max_i, max_d = yy, yd+d
  return max_i, max_d

y, d = dfs(1)
visited = [False]*(n+1)
_, d = dfs(y)
print(d)