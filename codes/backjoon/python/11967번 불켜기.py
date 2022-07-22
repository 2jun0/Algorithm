from collections import deque
import sys
INF = 10**10
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

N, M = input_n(int)
graph = [[[] for _ in range(N)] for _ in range(N)]
for _ in range(M):
  x, y, a, b = input_n(int)
  graph[x-1][y-1].append((a-1,b-1))

def bfs():
  cnt = 0
  has_light = [[False]*N for _ in range(N)]
  visited = [[False]*N for _ in range(N)]
  waitting = [[False]*N for _ in range(N)]
  q = deque()
  q_waitting = deque()
  q_rewaitting = deque()

  # i, j 에서 근처에 있는 불을 켬.
  def turn_on_from(i, j):
    nonlocal cnt, has_light

    for t_i, t_j in graph[i][j]:
      if not has_light[t_i][t_j]:
        has_light[t_i][t_j] = True
        cnt += 1

  # 대기 중인 노드들을 확인함.
  def check_watting_que():
    nonlocal q_waitting, q_rewaitting

    has_any_light = False
    
    while q_waitting:
      i, j = q_waitting.popleft()

      if has_light[i][j]:
        has_any_light = True

        turn_on_from(i,j)
        visited[i][j] = True
        q.append((i, j))
      else:
        q_rewaitting.append((i, j))

    return has_any_light

  cnt += 1
  has_light[0][0] = True
  turn_on_from(0,0)

  visited[0][0] = True
  q.append((0, 0))

  while q:
    while q:
      i, j = q.popleft()
      
      for t_i, t_j in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
        if 0<=t_i<N and 0<=t_j<N and not visited[t_i][t_j]:

          if has_light[t_i][t_j]:
            turn_on_from(t_i, t_j)
            visited[t_i][t_j] = True
            q.append((t_i, t_j))
          elif not waitting[t_i][t_j]:
            # 여기는 기다렸다가 큐가 비면, 확인해봄
            waitting[t_i][t_j] = True
            q_waitting.append((t_i, t_j))
    
    # 큐가 다 돌고 나서 조건이 맞는지 실행해봄.
    # 모두 다 맞지 않는 경우, 함수 종료
    if not check_watting_que():
      return cnt
    
    q_waitting, q_rewaitting = q_rewaitting, q_waitting

print(bfs())