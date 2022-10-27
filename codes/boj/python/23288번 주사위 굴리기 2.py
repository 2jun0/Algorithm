from collections import deque
import sys
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

EAST, NORTH, WEST, SOUTH = 0, 1, 2, 3

class Dice:
  def __init__(self):
    self.up = 1
    self.down = 6
    self.north = 2
    self.south = 5
    self.west = 4
    self.east = 3

    self.y = 0
    self.x = 0
    self.d = EAST

  def turn(self):
    if self.d == EAST:
      self.turn_east()
    elif self.d == NORTH:
      self.turn_north()
    elif self.d == WEST:
      self.turn_west()
    elif self.d == SOUTH:
      self.turn_south()
  
  def turn_north(self):
    self.down, self.north, self.up, self.south = self.north, self.up, self.south, self.down
    self.y -= 1

  def turn_south(self):
    self.down, self.north, self.up, self.south = self.south, self.down, self.north, self.up
    self.y += 1

  def turn_west(self):
    self.down, self.west, self.up, self.east = self.west, self.up, self.east, self.down
    self.x -= 1

  def turn_east(self):
    self.down, self.west, self.up, self.east = self.east, self.down, self.west, self.up
    self.x += 1

def get_same_num_cnt_bfs(N, M, table, sy, sx):
  '''sy, sx 부터 사방으로 같은 값을 가진 칸의 개수를 구함'''
  cnt = 0

  q = deque()
  visited = [[False] * M for _ in range(N)]

  q.append((sy,sx))
  visited[sy][sx] = True

  while q:
    y, x = q.popleft()
    cnt += 1

    for ny, nx in [(y-1,x), (y+1,x), (y,x+1), (y,x-1)]:
      if 0<=ny<N and 0<=nx<M and not visited[ny][nx] and table[sy][sx] == table[ny][nx]:
        visited[ny][nx] = True
        q.append((ny, nx))

  return cnt

def turn_dice(dice, N, M, table):
  '''주사위 굴리기'''

  dice.turn()
  if not (0<=dice.y<N and 0<=dice.x<M):
    # 주사기가 이동한 곳이 칸이 없는 곳이라면 반대로 한 다음 두 칸 굴러감
    dice.d = (dice.d + 2) % 4
    dice.turn()
    dice.turn()
  
  A = dice.down
  B = table[dice.y][dice.x]
  if A > B:
    dice.d = (dice.d - 1) % 4
  elif A < B:
    dice.d = (dice.d + 1) % 4

  return get_same_num_cnt_bfs(N, M, table, dice.y, dice.x) * B

N, M, K = input_n(int)
table = [input_n(int) for _ in range(N)]
dice = Dice()
score = 0

for _ in range(K):
  score += turn_dice(dice, N, M, table)

print(score)