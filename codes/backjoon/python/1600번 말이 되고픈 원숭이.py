from collections import deque
import sys
INF = 10**10
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

# 무향 그래프 문제
# 가중치가 같고 costs를 3차원으로 해야함.

K = input(int)
W, H = input_n(int)
table = [input_n(int) for _ in range(H)]

delta = [
  (1,0,0), (-1,0,0), (0,1,0), (0,-1,0), # 상하좌우 말X 
  (-2,-1,1), (-2,1,1), (-1,-2,1), (-1,2,1), (1,-2,1), (1,2,1), (2,-1,1), (2,1,1) # 말이 움직이는 것
  ]

def bfs():
  costs = [[[INF] * (K+1) for _ in range(W)] for _ in range(H)] # MAXIMUM 30 * 200 * 200 = 1,200,000

  costs[0][0][0] = 0
  q = deque([(0,0,0)]) # i, j, 말처럼 움직인 수

  while q:
    i,j,k = q.popleft()

    # 도착!
    if i == H-1 and j == W-1:
      return costs[i][j][k]

    for di, dj, dk in delta:
      t_i, t_j, t_k = i + di, j + dj, k + dk

      if 0<=t_i<H and 0<=t_j<W and t_k <= K: # index 범위 검사 : 말 이동 횟수, i, j 범위 검사
        # 이동 할 수 있고, 방문한 적 없어야 함
        if table[t_i][t_j] == 0 and costs[t_i][t_j][t_k] == INF:
          costs[t_i][t_j][t_k] = costs[i][j][k]+1
          q.append((t_i, t_j, t_k))

  return -1;
      
print(bfs())