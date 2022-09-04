from shutil import move
import sys
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
  return list(map(_type, input().split()))

def get_pos(y, x, d):
  if d == NORTH:
    return y-1, x
  elif d == EAST:
    return y, x+1
  elif d == SOUTH:
    return y+1, x
  elif d == WEST:
    return y, x-1

def start_cleaning(y, x, d):
  def move_forward(d):
    nonlocal y, x
    n_y, n_x = get_pos(y, x, d)
    if 0<=n_y<N and 0<=n_x<M and table[n_y][n_x] == 0:
      y, x = n_y, n_x
      return True
    return False
  
  def can_clean_forward(d):
    nonlocal y, x
    n_y, n_x = get_pos(y, x, d)
    if 0<=n_y<N and 0<=n_x<M and table[n_y][n_x] == 0 and not visited[n_y][n_x]:
      return True
    return False

  visited = [[False] * M for _ in range(N)]

  while True:
    # 1
    visited[y][x] = True

    # 2
    for left_d in [(d-i-1)%4 for i in range(4)]:
      # 2.1
      if can_clean_forward(left_d):
        move_forward(left_d)
        d = left_d
        break
      
      # 2.2
        # nothing
    else:
      back_d = (d+2)%4 # back

      # 2.3
      # try back forward
      if move_forward(back_d):
        pass # nothing
      # 2.4
      else:
        break

  return sum([sum(line) for line in visited])
    
NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

N, M = input_n(int)
y, x, d = input_n(int)
table = [input_n(int) for _ in range(N)]

print(start_cleaning(y, x, d))