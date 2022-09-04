import sys

INF = 10**8
def input(_type=str):
	return _type(sys.stdin.readline().rstrip())
def input_n(_type=str):
	return list(map(_type, input().split()))
def print_n(L):
  s = ''
  for l in L: s+='{} '.format(l)
  print(s[:-1])

N, M, V = input_n(int)
graph = [[] for _ in range(N+1)]
for _ in range(M):
  a,b = input_n(int)
  graph[a].append(b)
  graph[b].append(a)
for g in graph:
  g.sort()

def DFS():
  visited = [False]*(N+1)
  s = [V]
  results = []
  while len(s) > 0:
    x = s.pop()
    if visited[x]: continue
    visited[x] = True
    results.append(x)

    s.extend(graph[x][::-1])

  print_n(results)

def BFS():
  visited = [False]*(N+1)
  s1 = [[V]]
  results = []
  while len(s1) > 0:
    s2 = s1.pop(0)
    while len(s2) > 0:
      x = s2.pop(0)
      if visited[x]: continue
      visited[x] = True
      results.append(x)
      s2.extend(graph[x])

  print_n(results)

DFS()
BFS()
