import sys
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

class Pos:
  def __init__(self, y, x):
    self.y = y
    self.x = x

POS_LEFT_DOWN = 0
POS_RIGHT_DOWN = 1
POS_LEFT_UP = 2
POS_RIGHT_UP = 3

def turn_right(pos_order):
  # 1 2    
  # 0 3   
  # to
  # 0 1
  # 3 2 
  # 0 -> 3, 1 -> 0, 2 -> 1, 3 -> 2
  return (
    pos_order[1], pos_order[2], pos_order[3], pos_order[0]
  )

def turn_left(pos_order):
  # 1 2    
  # 0 3   
  # to
  # 2 3
  # 1 0 
  # 0 -> 1, 1 -> 2, 2 -> 3, 3 -> 0
  return (
    pos_order[3], pos_order[0], pos_order[1], pos_order[2]
  )

def find(num_start, num_end, pos_order, start_pos, end_pos, reverse_order, num):
  n = num_end-num_start

  if n == 1:
    return start_pos

  # 번호 범위가 몇 번째 부분집합에 있는가?
  nxt_nums = [
    (num_start+n//4*0, num_start+n//4*1), # 0
    (num_start+n//4*1, num_start+n//4*2), # 1
    (num_start+n//4*2, num_start+n//4*3), # 2
    (num_start+n//4*3, num_start+n//4*4), # 3
  ]

  idx = None
  for i in range(4):
    nxt_num_start, nxt_num_end = nxt_nums[i]

    if nxt_num_start <= num < nxt_num_end:
      idx = i
      break

  nxt_num_start, nxt_num_end = nxt_nums[idx]
  nxt_start_pos, nxt_end_pos = None, None

  mid_pos = Pos((start_pos.y+end_pos.y)//2, (start_pos.x+end_pos.x)//2)

  if reverse_order:
    idx = 4 - idx - 1

  if pos_order[idx] == POS_LEFT_DOWN:
    nxt_start_pos = start_pos
    nxt_end_pos = mid_pos
  elif pos_order[idx] == POS_LEFT_UP:
    nxt_start_pos = Pos(mid_pos.y, start_pos.x)
    nxt_end_pos = Pos(end_pos.y, mid_pos.x)
  elif pos_order[idx] == POS_RIGHT_DOWN:
    nxt_start_pos = Pos(start_pos.y, mid_pos.x)
    nxt_end_pos = Pos(mid_pos.y, end_pos.x)
  elif pos_order[idx] == POS_RIGHT_UP:
    nxt_start_pos = mid_pos
    nxt_end_pos = end_pos

  if idx == 0:
    return find(nxt_num_start, nxt_num_end, turn_right(pos_order), nxt_start_pos, nxt_end_pos, reverse_order ^ True, num)
  elif idx == 3:
    return find(nxt_num_start, nxt_num_end, turn_left(pos_order), nxt_start_pos, nxt_end_pos, reverse_order ^ True, num)
  else:
    return find(nxt_num_start, nxt_num_end, pos_order, nxt_start_pos, nxt_end_pos, reverse_order, num)


N, M = input_n(int)
pos = find(0, N*N, [
  POS_LEFT_DOWN,
  POS_LEFT_UP,
  POS_RIGHT_UP,
  POS_RIGHT_DOWN,
], Pos(0,0), Pos(N, N), False, M-1)
print(pos.x+1, pos.y+1)