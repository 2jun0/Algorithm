from copy import deepcopy
from itertools import permutations
import sys

def input(_type=str):
	return _type(sys.stdin.readline().rstrip())
def input_n(_type):
	return list(map(_type, input().split()))

RIGHT, DOWN, LEFT, UP = 0, 1, 2, 3
dy = [0,1,0,-1]
dx = [1,0,-1,0]

def get_a_v(table):
  '''A의 값은 각 행에 있는 모든 수의 합 중 최솟값'''
  return min(sum(row) for row in table)

def turn(table, new_table, r, c, d):
  '''table을 (r, c)을 중심으로 d칸 떨어져있는 정사각형을 시계방향으로 돌린 값을 nxt_table에 넣음'''

  if d == 0:
    # d가 0일때는 돌리는 연산을 하지 않는다.
    new_table[r][c] = table[r][c]
    return

  # 꼭짓점. 방향 바꾸는 곳.
  vertexes = [(r-d,c-d),(r-d,c+d),(r+d,c+d),(r+d,c-d)]

  dir = RIGHT
  
  end_pos = (r-d, c-d)
  y, x = r-d, c-d

  while True:
    nxt_y = y + dy[dir]
    nxt_x = x + dx[dir]

    new_table[nxt_y][nxt_x] = table[y][x]

    y, x = nxt_y, nxt_x

    if (y,x) == end_pos:
      break

    if (y,x) in vertexes:
      # 꼭짓점을 만나 오른쪽으로 90도 회전
      dir = (dir+1)%4

def main():
  N, M, K = input_n(int)
  origin_table = [input_n(int) for _ in range(N)]
  min_a_v = 10**8

  cmds = []
  for _ in range(K):
    _r, _c, s = input_n(int)
    r, c = _r-1, _c-1
    cmds.append((r,c,s))

  for order in permutations(cmds):
    table = origin_table

    for r, c, s in order:
      new_table = deepcopy(table)
      for d in range(1, s+1):
        turn(table, new_table, r, c, d)
      table = new_table
    
    min_a_v = min(min_a_v, get_a_v(table))

  print(min_a_v)

main()