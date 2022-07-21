from collections import deque
import sys
INF = 10**10
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

N, M, K = input_n(int)
table = [list(map(int, input())) for _ in range(N)]

def bfs():
  q = deque()
  dists = [[[INF]*(K+1) for _ in range(M)] for _ in range(N)]

  dists[0][0][0] = 1
  q.append((0,0,0))

  while q:
    i,j,k = q.popleft()

    if i == N-1 and j == M-1:
      return dists[i][j][k]

    for t_i, t_j in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
      if 0<=t_i<N and 0<=t_j<M:
        # 벽이 없다
        if table[t_i][t_j] == 0 and dists[t_i][t_j][k] == INF:
          dists[t_i][t_j][k] = dists[i][j][k]+1
          q.append((t_i,t_j,k))
        # 벽이 있지만 더 부술 수 있다
        elif k+1 <= K and dists[t_i][t_j][k+1] == INF:
          dists[t_i][t_j][k+1] = dists[i][j][k]+1
          q.append((t_i,t_j,k+1))

  return -1

print(bfs())
