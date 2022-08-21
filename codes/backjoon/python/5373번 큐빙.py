import sys
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

UP, DOWN, FRONT, BACK, LEFT, RIGHT = 'U', 'D', 'F', 'B', 'L', 'R'

DIR = {
  'NW': (0,0),
  'NN': (0,1),
  'NE': (0,2),
  'WW': (1,0),
  'EE': (1,2),
  'SW': (2,0),
  'SS': (2,1),
  'SE': (2,2),
}

adj_plates_by_direction = {
  UP : { 'N': BACK, 'E': RIGHT, 'S': FRONT, 'W': LEFT },
  DOWN : { 'N': FRONT, 'E': RIGHT, 'S': BACK, 'W': LEFT },
  RIGHT : { 'N': UP, 'E': BACK, 'S': DOWN, 'W': FRONT },
  FRONT : { 'N': UP, 'E': RIGHT, 'S': DOWN, 'W': LEFT },
  LEFT : { 'N': UP, 'E': FRONT, 'S': DOWN, 'W': BACK },
  BACK : { 'N': UP, 'E': LEFT, 'S': DOWN, 'W': RIGHT }
}

directions_by_adj_plate = {
  UP : { BACK:'N', RIGHT:'E', FRONT:'S', LEFT:'W' },
  DOWN : { FRONT:'N', RIGHT:'E', BACK:'S', LEFT:'W' },
  RIGHT : { UP:'N', BACK:'E', DOWN:'S', FRONT:'W' },
  FRONT : { UP:'N', RIGHT:'E', DOWN:'S', LEFT:'W' },
  LEFT : { UP:'N', FRONT:'E', DOWN:'S', BACK:'W' },
  BACK : { UP:'N', LEFT:'E', DOWN:'S', RIGHT:'W' }
}

# NN => 나의 North에 있는 면의 North는 나
# EN => 나의 East에 있는 면의 North는 나

# UP : NN(0,2)(0,1)(0,0), EN(0,2)(0,1)(0,0), SN(0,2)(0,1)(0,0), WN(0,2)(0,1)(0,0),
# DOWN : NS(2,0)(2,1)(2,2), ES(2,0)(2,1)(2,2), SS(2,0)(2,1)(2,2), WS(2,0)(2,1)(2,2),
# RIGHT : NE(2,2)(1,2)(0,2), EW(0,0)(1,0)(2,0), SE(2,2)(1,2)(0,2), WE(2,2)(1,2)(0,2),
# FRONT : NS(2,0)(2,1)(2,2), EW(0,0)(1,0)(2,0), SN(0,2)(0,1)(0,0), WE(2,2)(1,2)(0,2),
# LEFT : NW(0,0)(1,0)(2,0), EW(0,0)(1,0)(2,0), SW(0,0)(1,0)(2,0), WE(2,2)(1,2)(0,2),
# BACK : NN(0,2)(0,1)(0,0), EW(0,0)(1,0)(2,0), SS(2,0)(2,1)(2,2), WE(2,2)(1,2)(0,2),

# 인접 면의 내 면이 닿은 방향을 알아야 한다.
# directions_by_adj_plate[adj_plates_by_direction[ME][dir]][ME]

turn_preset = {
  'N': [(0,2),(0,1),(0,0)],
  'E': [(2,2),(1,2),(0,2)],
  'S': [(2,0),(2,1),(2,2)],
  'W': [(0,0),(1,0),(2,0)],
}

def turn(cube, plate, is_clockwise):
  order = [(0,0),(0,1),(0,2),(1,2),(2,2),(2,1),(2,0),(1,0)]
  if not is_clockwise:
    order = order[::-1]

  for _ in range(2):
    y, x = order[0]
    start = cube[plate][y][x]
    for order_idx in range(7, 0, -1):
      y, x = order[order_idx]
      n_y, n_x = order[(order_idx+1)%8]
      cube[plate][n_y][n_x] = cube[plate][y][x]
    y, x = order[0]
    n_y, n_x = order[1]
    cube[plate][n_y][n_x] = start

  # adj plates
  adj_order = []
  for dir in ['N', 'E', 'S', 'W']:
    adj_plate = adj_plates_by_direction[plate][dir]
    for y, x in turn_preset[directions_by_adj_plate[adj_plate][plate]]:
      adj_order.append((adj_plate,y,x))

  if not is_clockwise:
    adj_order = adj_order[::-1]

  for _ in range(3):
    adj_plate, y, x = adj_order[0]
    start = cube[adj_plate][y][x]
    for order_idx in range(11, 0, -1):
      adj_plate, y, x = adj_order[order_idx]
      n_adj_plate, n_y, n_x = adj_order[(order_idx+1)%12]
      cube[n_adj_plate][n_y][n_x] = cube[adj_plate][y][x]
    adj_plate, y, x = adj_order[0]
    n_adj_plate, n_y, n_x = adj_order[1]
    cube[n_adj_plate][n_y][n_x] = start

def print_up(cube):
  for line in cube[UP]:
    print(''.join(line))
# def print_all(cube):
#   for plate in cube.keys():
#     print(plate)
#     for line in cube[plate]:
#       print(''.join(line))

T = input(int)
for _ in range(T):
  cube = {
    UP: [['w']*3 for _ in range(3)],
    DOWN: [['y']*3 for _ in range(3)],
    FRONT: [['r']*3 for _ in range(3)],
    BACK: [['o']*3 for _ in range(3)],
    LEFT: [['g']*3 for _ in range(3)],
    RIGHT: [['b']*3 for _ in range(3)],
  }

  n = input(int)

  cmds = input_n(str)

  for cmd in cmds:
    turn(cube, cmd[0], cmd[1] == '+')
  print_up(cube)
    