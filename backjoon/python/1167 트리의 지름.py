import sys
sys.setrecursionlimit(10000000) # 재귀 제한 풀기
INF = 10**8
def input(_type=str):
	return _type(sys.stdin.readline().rstrip())
def input_n(_type=str):
	return list(map(_type, input().split()))
def print_n(L):
  s = ''
  for l in L: s+='{} '.format(l)
  print(s[:-1])

V = input(int)

graph = [[] for _ in range(V+1)]
for _ in range(V):
  L = input_n(int)
  x = L[0]
  for i in range(len(L)//2-1):
    y = L[1+2*i]
    d = L[2+2*i]
    graph[x].append((y,d))

visited = [False] * (V+1)
def dfs(x):
  if visited[x]: return 0, 0
  visited[x] = True
  max_d, max_i = 0, 0
  for y, d in graph[x]:
    tmp_d, tmp_i = dfs(y)
    tmp_d += d
    if tmp_i == 0: continue
    if max_d < tmp_d: max_d, max_i = tmp_d, tmp_i
  if max_i == 0: max_i = x
  return max_d, max_i

d, i = dfs(1)
visited = [False] * (V+1)
d, i = dfs(i)
print(d)