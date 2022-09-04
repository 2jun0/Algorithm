import sys
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

N = 0
S = 1
def score_gears():
  score = 0
  if gears[0][gears_tops[0]] == S: score+=1
  if gears[1][gears_tops[1]] == S: score+=2
  if gears[2][gears_tops[2]] == S: score+=4
  if gears[3][gears_tops[3]] == S: score+=8
  return score

def is_stick_together(left_idx, right_idx):
  left_idx, right_idx = min(left_idx, right_idx), max(left_idx, right_idx)

  left_v = gears[left_idx][(gears_tops[left_idx]+2) % 8]
  right_v = gears[right_idx][(gears_tops[right_idx]-2) % 8]
  return left_v != right_v

RIGHT = 1
LEFT = -1
def turn_gear(idx, direction, _ignore_n_idx):
  if direction == RIGHT:
    # idx-1 : left
    # idx+1 : right
    for n_idx in [(idx-1), (idx+1)]:
      if 0<=n_idx<4 and n_idx != _ignore_n_idx and is_stick_together(idx, n_idx):
        turn_gear(n_idx, LEFT, idx)
    gears_tops[idx] = (gears_tops[idx] - 1) % 8

  if direction == LEFT:
    for n_idx in [(idx-1), (idx+1)]:
      if 0<=n_idx<4 and n_idx != _ignore_n_idx and is_stick_together(idx, n_idx):
          turn_gear(n_idx, RIGHT, idx)
    gears_tops[idx] = (gears_tops[idx] + 1) % 8

gears = [list(map(int, input())) for _ in range(4)]
gears_tops = [0]*4
K = input(int)
for _ in range(K):
  # _idx = idx + 1
  _idx, direction = input_n(int)
  turn_gear(_idx-1, direction, None)

print(score_gears())
