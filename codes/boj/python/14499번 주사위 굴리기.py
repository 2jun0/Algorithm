import sys
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
  return list(map(_type, input().split()))

def turn_dice(direction):
  if direction == RIGHT:
    dice_map[RIGHT], dice_map[DOWN], dice_map[LEFT], dice_map[UP] \
    = \
    dice_map[UP], dice_map[RIGHT], dice_map[DOWN], dice_map[LEFT]

  elif direction == LEFT:
    dice_map[LEFT], dice_map[UP], dice_map[RIGHT], dice_map[DOWN] \
    = \
    dice_map[UP], dice_map[RIGHT], dice_map[DOWN], dice_map[LEFT]

  elif direction == UP:
    dice_map[BACK], dice_map[UP], dice_map[FRONT], dice_map[DOWN] \
    = \
    dice_map[UP], dice_map[FRONT], dice_map[DOWN], dice_map[BACK]
    
  elif direction == DOWN:
    dice_map[FRONT], dice_map[DOWN], dice_map[BACK], dice_map[UP] \
    = \
    dice_map[UP], dice_map[FRONT], dice_map[DOWN], dice_map[BACK]

def move_dice(direction):
  global dice_y, dice_x
  nxt_y, nxt_x = dice_y, dice_x

  if direction == RIGHT:
    nxt_x += 1
  elif direction == LEFT:
    nxt_x -= 1
  elif direction == UP:
    nxt_y -= 1
  elif direction == DOWN:
    nxt_y += 1
  
  if 0<=nxt_y<N and 0<=nxt_x<M:
    dice_y, dice_x = nxt_y, nxt_x
    return True
  else:
    return False

RIGHT = 1
LEFT = 2
UP = 3
DOWN = 4
# for dice map
BACK = 5
FRONT = 6

N, M, dice_y, dice_x, K = input_n(int)
table = [input_n(int) for _ in range(N)]

dice_map = {
  RIGHT: 0, LEFT: 0, UP: 0, DOWN: 0, BACK: 0, FRONT: 0
}

for direction in input_n(int):
  if move_dice(direction):
    turn_dice(direction)

    if table[dice_y][dice_x] == 0:
      table[dice_y][dice_x] = dice_map[DOWN]
    else:
      dice_map[DOWN] = table[dice_y][dice_x]
      table[dice_y][dice_x] = 0
    print(dice_map[UP])