import sys

def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

UP, LEFT, DOWN, RIGHT = 0, 1, 2, 3
dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]

def travel(table, y, x, dir):
  if (0<=y<N and 0<=x<M) and table[y][x] == 1:
    if dir == UP:
      dir = RIGHT
    elif dir == RIGHT:
      dir = UP
    elif dir == DOWN:
      dir = LEFT
    elif dir == LEFT:
      dir = DOWN
    
  return y+dy[dir], x+dx[dir], dir
    
def out_num(y, x):
  if x < 0:
    return y+1
  if x >= M:
    return (N-y) + N + M
  if y < 0:
    return (M-x) + N+M+N
  if y >= N:
    return x + N+ 1
  
  return -1

def out_pos(num):
  if num <= N:
    return num-1, -1, RIGHT
  elif num <= N+M:
    return N, num - N - 1, UP
  elif num <= N+M+N:
    return N-(num-N-M), M, LEFT
  else:
    return -1, M-(num-N-M-N), DOWN

N, M = input_n(int)
table = [input_n(int) for _ in range(N)]
nums = []
for num in range(1, N+M+N+M+1):
  y, x, d = out_pos(num)
  while True:
    y, x, d = travel(table, y, x, d)
    if not (0<=y<N and 0<=x<M):
      nums.append(out_num(y, x))
      break
      
print(*nums)