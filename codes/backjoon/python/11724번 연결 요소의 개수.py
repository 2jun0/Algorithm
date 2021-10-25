import sys

INF = 10**8
def input(_type=str):
	return _type(sys.stdin.readline().rstrip())
def input_n(_type=str):
	return list(map(_type, input().split()))

N, M = input_n(int)
graph = [[] for _ in range(N+1)]
for _ in range(M):
  u, v = input_n(int)
  graph[u].append(v)
  graph[v].append(u)

visited = [False] * (N+1)
s = []
cnt = 0

while True:
  finished = True
  for i in range(1, N+1):
    if not visited[i]:
      s.append(i)
      finished = False
      break

  if finished: break

  cnt += 1
  while len(s) > 0:
    x = s.pop()
    if visited[x]: continue
    visited[x] = True

    s.extend(graph[x])

print(cnt)