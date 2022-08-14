from collections import deque
import sys

INF = 10**10
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

LEFT, RIGHT, UP, DOWN = (0,-1), (0,1), (-1,0), (1,0)
def move_forward(pos, other_pos, d):
  y, x = pos

  while 0<=y+d[0]<N and 0<=x+d[1]<M and table[y+d[0]][x+d[1]] != '#' and (y+d[0], x+d[1]) != other_pos:
    if (y+d[0], x+d[1]) == hole:
      return (-1, -1)

    y, x = y+d[0], x+d[1]
    
  return (y, x)

def bfs(red, blue):
  costs = [[[[-1]*M for _ in range(N)] for _ in range(M)] for _ in range(N)]
  q = deque()
  costs[red[0]][red[1]][blue[0]][blue[1]] = 0
  q.append((red, blue))

  while q:
    red, blue = q.popleft()

    if costs[red[0]][red[1]][blue[0]][blue[1]] > 10 or blue == (-1,-1):
      continue

    if red == (-1,-1):
      return costs[red[0]][red[1]][blue[0]][blue[1]]

    for d in [LEFT, RIGHT, UP, DOWN]:
      n_red = move_forward(red, blue, d)
      n_blue = move_forward(blue, n_red, d)
      n_red = move_forward(n_red, n_blue, d) # red가 더 움직일 수 있을 경우

      if costs[n_red[0]][n_red[1]][n_blue[0]][n_blue[1]] == -1:
        costs[n_red[0]][n_red[1]][n_blue[0]][n_blue[1]] = costs[red[0]][red[1]][blue[0]][blue[1]] + 1
        q.append((n_red, n_blue))

  return -1

N, M = input_n(int)

table = [input(str) for _ in range(N)]
red, blue, hole = None, None, None

for y in range(N):
  for x in range(M):
    if table[y][x] == 'R': 
      red = (y,x)
    elif table[y][x] == 'B': 
      blue = (y,x)
    elif table[y][x] == 'O': 
      hole = (y,x)

print(bfs(red, blue))