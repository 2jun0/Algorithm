from collections import deque
import sys

def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

N, M = input_n(int)
table = [input_n(int) for _ in range(N)]

def func():
  global table

  q = deque()
  q_nxt = deque()

  has_chunk = [[False] * M for _ in range(N)]

  years = 0

  # 초기 빙산 찾기 
  for i in range(N):
    for j in range(M):
      if table[i][j] > 0:
        q.append((i,j))

  while q:
    # 덩어리를 확인하기 위한 큐
    # 첫번째 값에 속해있는 덩어리만 체크한다.
    # 덩어리에 포함되어 있지 않으면 여러개로 판단
    has_chunk = [[False] * M for _ in range(N)]
    has_chunk[q[0][0]][q[0][1]] = True
    flag_q = deque([q[0]])
    while flag_q:
      i, j = flag_q.popleft()

      for t_i, t_j in [(i+1, j),(i-1, j),(i, j+1),(i, j-1)]:
        if 0<=t_i<N and 0<=t_j<M:
          if table[t_i][t_j] > 0 and not has_chunk[t_i][t_j]:
            has_chunk[t_i][t_j] = True
            flag_q.append((t_i, t_j))

    # 덩어리 확인 & 녹임 (table) -> 효율성을 위해 같은 for문에 구현
    table_nxt = [[0] * M for _ in range(N)]
    while q:
      i, j = q.popleft()

      # 다른 덩어리에 있는 경우 -> 덩어리가 2개이상이다.
      if not has_chunk[i][j]:
        return years

      table_nxt[i][j] = table[i][j]
      for t_i, t_j in [(i+1, j),(i-1, j),(i, j+1),(i, j-1)]:
        if 0<=t_i<N and 0<=t_j<M:
          # 근처의 칸이 바다면 하나씩 녹임
          if table[t_i][t_j] == 0:
            table_nxt[i][j] = max(table_nxt[i][j] - 1, 0)
        
      # 내가 녹지 않았다면 다음 큐에 저장
      if table_nxt[i][j] > 0:
        q_nxt.append((i,j))

    table_nxt, table = table, table_nxt
    q, q_nxt = q_nxt, q
    years += 1

  # 못찾은 경우 -> 다 녹은 것.
  return 0

print(func())