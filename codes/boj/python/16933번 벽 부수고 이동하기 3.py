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
  q = deque() # 현재 큐
  q_nxt = deque() # 다음 큐
  q_nxt_nxt = deque() # 다다음 큐

  dists = [[[INF]*(K+1) for _ in range(M)] for _ in range(N)]

  dists[0][0][0] = 1
  # i, j, k
  q.append((0,0,0))
  is_daytime = True

  while q:
    while q:
      i,j,k = q.popleft()

      if i == N-1 and j == M-1:
        return dists[i][j][k]

      for t_i, t_j in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
        if 0<=t_i<N and 0<=t_j<M:

          # 벽이 없다
          if table[t_i][t_j] == 0 and dists[t_i][t_j][k] > dists[i][j][k]+1:
            dists[t_i][t_j][k] = dists[i][j][k]+1
            q_nxt.append((t_i,t_j,k))

          # 부실 수 있는 벽이 있다.
          if table[t_i][t_j] == 1 and k+1 <= K:
            # 낮이면 다음 큐에 넣는다
            if is_daytime and dists[t_i][t_j][k+1] > dists[i][j][k]+1:
              dists[t_i][t_j][k+1] = dists[i][j][k]+1
              q_nxt.append((t_i,t_j,k+1))
            # 밤이면 다다음 큐에 넣는다 (하루 쉬엇다고 생각)
            if not is_daytime and dists[t_i][t_j][k+1] > dists[i][j][k]+2:
              dists[t_i][t_j][k+1] = dists[i][j][k]+2
              q_nxt_nxt.append((t_i,t_j,k+1))

    is_daytime = not is_daytime
    q, q_nxt, q_nxt_nxt = q_nxt, q_nxt_nxt, q
    if not q: # 
      q, q_nxt, q_nxt_nxt = q_nxt, q_nxt_nxt, q
      
  return -1

print(bfs())
