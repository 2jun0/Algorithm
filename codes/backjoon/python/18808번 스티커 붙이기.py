import sys
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

def turn_right(sticker):
  # A B     E C A
  # C D  -> F D B
  # E F
  R, C = len(sticker), len(sticker[0])
  n_sticker = [[0]*R for _ in range(C)]

  for y in range(R):
    for x in range(C):
      n_sticker[x][R-y-1] = sticker[y][x]
  
  return n_sticker

def try_occupy(table, sticker):
  N, M = len(table), len(table[0])
  R, C = len(sticker), len(sticker[0])
  def _can_occupy(start_y, start_x):
    # out of range
    if not (0<=start_y+R-1<N and 0<=start_x+C-1<M):
      return False

    for s_y in range(R):
      for s_x in range(C):
        y = start_y + s_y
        x = start_x + s_x
        # failed!
        if sticker[s_y][s_x] == 1 and table[y][x] == 1:
          return False
    return True
  def _occupy(start_y, start_x):
    for s_y in range(R):
      for s_x in range(C):
        y = start_y + s_y
        x = start_x + s_x
        if sticker[s_y][s_x] == 1:
          table[y][x] = sticker[s_y][s_x]

  for y in range(N):
    for x in range(M):
      if _can_occupy(y,x):
        _occupy(y,x)
        return True
  return False

N, M, K = input_n(int)
table = [[0]*M for _ in range(N)]
for _ in range(K):
  R, C = input_n(int)
  sticker = [input_n(int) for _ in range(R)]

  for i in range(4):
    if try_occupy(table, sticker):
      break

    if i < 3:
      sticker = turn_right(sticker)

cnt_occupied = sum([sum(table[y]) for y in range(N)])
print(cnt_occupied)