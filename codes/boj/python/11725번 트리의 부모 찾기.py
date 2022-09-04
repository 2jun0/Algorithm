import sys
sys.setrecursionlimit(10000000) # 재귀 제한 풀기
INF = 10**8
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))
def print_n(L, join_str=' '):
  for i,l in enumerate(L): print(l, end=join_str if i<len(L)-1 else '\n')

N = input(int)
graph=[[]for _ in range(N+1)]
for _ in range(N-1):
  a,b = input_n(int)
  graph[a].append(b)
  graph[b].append(a)

parent=[0]*(N+1)
s = [(1, 0)]
visited=[False]*(N+1)
while len(s) > 0:
  x, p = s.pop()
  if visited[x]: continue
  visited[x] = True
  parent[x] = p
  for y in graph[x]: s.append((y,x))
for i in range(2, N+1): print(parent[i])