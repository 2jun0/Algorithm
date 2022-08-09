from collections import deque
import sys

def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
  return list(map(_type, input().split()))

N = input(int)
K = input(int)
table = [[0]*N for _ in range(N)]
for _ in range(K):
  y, x = input_n(int)
  table[y-1][x-1] = 1

L = input(int)

NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

def play(cmds):
  def turn_left():
    nonlocal d
    d=(d-1)%4
  def turn_right():
    nonlocal d
    d=(d+1)%4
  def move_forward():
    y, x = pos_q[-1]

    if d == NORTH:
      n_y, n_x = y-1, x
    elif d == EAST:
      n_y, n_x = y, x+1
    elif d == SOUTH:
      n_y, n_x = y+1, x
    elif d == WEST:
      n_y, n_x = y, x-1

    # collapse
    if not (0<=n_y<N and 0<=n_x<N) or table[n_y][n_x] == -1:
      return False
    
    if table[n_y][n_x] != 1:
      y, x = pos_q.popleft()
      table[y][x] = 0
    
    pos_q.append((n_y, n_x))
    table[n_y][n_x] = -1

    return True

  pos_q, d = deque([(0,0)]), EAST
  table[0][0] = -1
  time = 0

  for X, C in cmds:
    while time < X:
      time+=1
      if not move_forward():
        return time
    
    if C == 'L':
      turn_left()
    else:
      turn_right()
    
  while True:
    time+=1
    if not move_forward():
      return time
  
cmds = []
for _ in range(L):
  X, C = input_n(str)
  cmds.append((int(X), C))

print(play(cmds))