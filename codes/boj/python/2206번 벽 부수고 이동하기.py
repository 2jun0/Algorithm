import sys
from collections import deque

INF = 10**8
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

N, M = input_n(int)
table = []
for _ in range(N):
  table.append(list(map(int, input())))

def bfs():
  dist = [[[INF] * 2 for _ in range(M)] for _ in range(N)]
  dist[0][0][0] = 1

  # i, j, break?
  q = deque()
  q.append((0,0,0))
  while q:
    i, j, b = q.popleft()

    # 도착지에 도달했으면 끝
    if i == N-1 and j == M-1:
      return dist[i][j][b]

    for t_i, t_j in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
      if 0<=t_i<N and 0<=t_j<M:
        # 갈 수 있고, 방문하지 않음
        if table[t_i][t_j] == 0 and dist[t_i][t_j][b] == INF:
          dist[t_i][t_j][b] = dist[i][j][b]+1
          q.append((t_i, t_j, b))
        # 벽이 있고 부술 수 있음
        if table[t_i][t_j] == 1 and b == 0:
          dist[t_i][t_j][1] = dist[i][j][b]+1
          q.append((t_i, t_j, 1))
      
  return -1

print(bfs())