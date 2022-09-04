import sys

def input(_type=str):
	return _type(sys.stdin.readline().rstrip())
def input_n(_type):
	return list(map(_type, input().split()))

N = input(int)
M = input(int)
graph = [[] for _ in range(N+1)]
for _ in range(M):
  a, b = input_n(int)
  graph[a].append(b)
  graph[b].append(a)

visited = [False] * (N+1)
s = [1]
while len(s) > 0:
  num = s.pop()
  if visited[num]: continue
  visited[num] = True
  s.extend(graph[num])

cnt = 0
for v in visited:
  if v: cnt+=1
print(cnt-1)
