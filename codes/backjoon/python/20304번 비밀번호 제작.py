from collections import deque
import sys
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

N = input(int)
M = input(int)
P = input_n(int)

def bfs():
  visited = [-1] * (N+1)

  q = deque()
  
  for p in P:
    visited[p] = 0
    q.append(p)

  while q:
    x = q.popleft()

    for i in range(20):
      nxt = x ^ (1 << i)

      if nxt >= N and visited[nxt] != -1:
        visited[nxt] = visited[x] + 1
        q.append(nxt)

  return max(visited)

print(bfs())