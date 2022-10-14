from collections import deque
import sys
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

RIGHT, DOWN, RIGHT_DOWN = 0, 1, 2

dy = { RIGHT: 0, DOWN: 1, RIGHT_DOWN: 1 }
dx = { RIGHT: 1, DOWN: 0, RIGHT_DOWN: 1 }

NEXT_DS = {
  RIGHT: [RIGHT, RIGHT_DOWN], 
  DOWN: [DOWN, RIGHT_DOWN], 
  RIGHT_DOWN: [RIGHT, DOWN, RIGHT_DOWN]
}

def can_occupy(table,d,y,x):
  '''d방향으로 y,x에 파이프를 둘 수 있는가?'''
  if d in [RIGHT, DOWN]:
    return table[y][x] != 1
  elif d == RIGHT_DOWN:
    return table[y][x] != 1 and table[y-1][x] != 1 and table[y][x-1] != 1

def get_case_cnt_bfs(N, table, srt_y, srt_x, srt_d):
  cnts = [[[0]*3 for _ in range(N)] for _ in range(N)]
  visited = [[[False]*3 for _ in range(N)] for _ in range(N)]
  q = deque()

  cnts[srt_y][srt_x][srt_d] = 1
  visited[srt_y][srt_x][srt_d] = True
  q.append((srt_y, srt_x, srt_d))

  while q:
    y, x, d = q.popleft()

    for nd in NEXT_DS[d]:
      ny, nx = y + dy[nd], x + dx[nd]

      if 0<=ny<N and 0<=nx<N:
        if not visited[ny][nx][nd]:
          # 이번에 처음 가본 경우
          visited[ny][nx][nd] = True
          q.append((ny,nx,nd))

        if can_occupy(table, nd, ny, nx):
          # 파이프를 둘 수 있나?
          cnts[ny][nx][nd] += cnts[y][x][d]

  return sum(cnts[N-1][N-1])


N = int(input())
table = [input_n(int) for _ in range(N)]
print(get_case_cnt_bfs(N, table, 0, 1, RIGHT))