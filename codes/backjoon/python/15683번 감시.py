import sys
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

N, M = input_n(int)
table = [input_n(int) for _ in range(N)]
can_watch = [[0]*M for _ in range(N)]

CCTVS = []
cnt_walls = 0
for y in range(N):
  for x in range(M):
    if 1 <= table[y][x] <= 5:
      CCTVS.append((y,x))
    elif table[y][x] == 6:
      cnt_walls += 1


UP = (-1,0)
DOWN = (1,0)
LEFT = (0,-1)
RIGHT = (0,1)
# return : 새로 감시하는 칸 개수
def turn_on_CCTV(y, x, angle, v = 1):
  def watch_toward(dy, dx):
    cnt = 0
    ty, tx = y, x
    while 0 <= ty < N and 0 <= tx < M and table[ty][tx] != 6:
      # 처음 감시하는 곳을 센다.
      if can_watch[ty][tx] == 0:
        cnt += 1
      can_watch[ty][tx] += v

      ty += dy
      tx += dx
    
    return cnt

  dyx = None
  if table[y][x] == 1:
    if angle == 0: dyx = [RIGHT]
    elif angle == 1: dyx = [DOWN]
    elif angle == 2: dyx = [LEFT]
    elif angle == 3: dyx = [UP]

  if table[y][x] == 2:
    if angle == 0 or angle == 2:
      dyx = [RIGHT, LEFT]
    elif angle == 1 or angle == 3:
      dyx = [DOWN, UP]
    
  if table[y][x] == 3:
    if angle == 0: dyx = [UP, RIGHT]
    elif angle == 1: dyx = [RIGHT, DOWN]
    elif angle == 2: dyx = [DOWN, LEFT]
    elif angle == 3: dyx = [LEFT, UP]

  if table[y][x] == 4:
    if angle == 0: dyx = [LEFT, UP, RIGHT]
    elif angle == 1: dyx = [UP, RIGHT, DOWN]
    elif angle == 2: dyx = [RIGHT, DOWN, LEFT]
    elif angle == 3: dyx = [DOWN, LEFT, UP]
  
  if table[y][x] == 5:
    dyx = [LEFT, UP, RIGHT, DOWN]
  
  cnt = 0
  for dy, dx in dyx:
    cnt += watch_toward(dy, dx)
  return cnt

def dfs(i, angle):
  y,x = CCTVS[i]
  # 켜기
  this_cnt = turn_on_CCTV(y,x,angle)
  max_nxt_cnt = 0
  if i+1 < len(CCTVS):
    for n_angle in range(4):
      max_nxt_cnt = max(max_nxt_cnt, dfs(i+1, n_angle))
  # 끄기
  turn_on_CCTV(y,x,angle,-1)
  return this_cnt + max_nxt_cnt

max_cnt = 0
if 0 < len(CCTVS):
  for angle in range(4):
    max_cnt = max(max_cnt, dfs(0, angle))

print(N*M - cnt_walls - max_cnt)