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

T = input(int)
for _ in range(T):
  n = input(int)
  pos = [input_n(int) for __ in range(n+2)]

  graph = [[] for _ in range(n+2)]
  for i in range(n+2):
    for j in range(n+2):
      if i==j or j==0: continue
      d = abs(pos[i][0]-pos[j][0]) + abs(pos[i][1]-pos[j][1])
      if d <= 1000:
        graph[i].append(j)
  
  visited = [False]*(n+2)
  s = [0]
  while len(s) > 0:
    x = s.pop()
    if visited[x]: continue
    visited[x] = True
    s.extend(graph[x])
  if visited[n+1]: print('happy')
  else: print('sad')