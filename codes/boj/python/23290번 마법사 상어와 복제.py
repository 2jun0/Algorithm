import sys
from collections import deque

def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

class Shark:
  dy = [-1, 0, 1, 0]
  dx = [0, -1, 0, 1]

  def __init__(self, y, x):
    self.y = y
    self.x = x

class Fish:
  dy = [0, -1, -1, -1, 0, 1, 1, 1]
  dx = [-1, -1, 0, 1, 1, 1, 0, -1]

  def __init__(self, y, x, d):
    self.y = y
    self.x = x
    self.d = d
  
  def move(self, smell_table, shark):
    '''물고기 이동, 상태만 변화함
    - Return : 이동 성공 여부
    '''
    nxt_d, nxt_y, nxt_x = self.get_nxt_transform(smell_table, shark)

    if nxt_d == -1:
      return False

    self.d, self.y, self.x = nxt_d, nxt_y, nxt_x
    return True

  def get_nxt_transform(self, smell_table, shark):
    '''다음 이동할 좌표와 방향 구하기
    - 이동할 수 없다면 -1, -1, -1을 반환한다.
    '''
    for dd in range(8):
      nxt_d = (self.d - dd) % 8
      nxt_y = self.y + Fish.dy[nxt_d]
      nxt_x = self.x + Fish.dx[nxt_d]

      if 0<=nxt_y<4 and 0<=nxt_x<4 and smell_table[nxt_y][nxt_x] == 0 and (nxt_y, nxt_x) != (shark.y, shark.x):
        return nxt_d, nxt_y, nxt_x
    return -1, -1, -1

  def get_clone(self):
    return Fish(self.y, self.x, self.d)

def copy_fishes(fish_table, nxt_fish_table):
  '''모든 물고기 복사'''
  for y in range(4):
    for x in range(4):
      for fish in fish_table[y][x]:
        nxt_fish_table[y][x].append(fish.get_clone())

def move_fishes(fish_table, smell_table, shark, nxt_fish_table):
  '''모든 물고기 이동'''
  def move_fish(fish: Fish):
    nonlocal nxt_fish_table
    fish.move(smell_table, shark)
    nxt_fish_table[fish.y][fish.x].append(fish)
  
  for y in range(4):
    for x in range(4):
      for fish in fish_table[y][x]:
        move_fish(fish)

def move_shark(shark, fish_table, smell_table):
  '''상어 움직임'''
  q = deque()
  q.append((shark.y, shark.x, (), (), 0))

  cases = []

  while q:
    y, x, log_d, log_pos, cost = q.popleft()
    dist = len(log_d)

    if dist == 3:
      cases.append((-cost, log_d, log_pos, y, x))
      continue

    for sd in range(4):
      nxt_y = y + Shark.dy[sd]
      nxt_x = x + Shark.dx[sd]

      if not (0<=nxt_y<4 and 0<=nxt_x<4):
        continue

      nxt_log_d = (*log_d, sd)
      nxt_log_pos = (*log_pos, (nxt_y, nxt_x))

      if (nxt_y, nxt_x) in log_pos:
        q.append((nxt_y, nxt_x, nxt_log_d, nxt_log_pos, cost))
      else:
        q.append((nxt_y, nxt_x, nxt_log_d, nxt_log_pos, cost+len(fish_table[nxt_y][nxt_x])))

  cases.sort()
  _, log_d, log_pos, ny, nx = cases[0]
  shark.y, shark.x = ny, nx

  for y, x in log_pos:
    if fish_table[y][x]:
      smell_table[y][x] = 3
      fish_table[y][x] = []

def remove_smell(smell_table):
  '''냄새 줄이기'''
  for y in range(4):
    for x in range(4):
      if smell_table[y][x]:
        smell_table[y][x] = max(0, smell_table[y][x]-1)

fish_table = [[[] for _ in range(4)] for _ in range(4)]
smell_table = [[0]*4 for _ in range(4)]
shark = None

M, S = input_n(int)

for _ in range(M):
  _fy, _fx, _fd = input_n(int)
  fx, fy, fd = _fx-1, _fy-1, _fd-1
  fish_table[fy][fx].append(Fish(fy, fx, fd))

_sy, _sx = input_n(int)
shark = Shark(_sy - 1, _sx - 1)

for _ in range(S):
  copied_fish_table = [[[] for _ in range(4)] for _ in range(4)]
  copy_fishes(fish_table, copied_fish_table)

  moved_fish_table = [[[] for _ in range(4)] for _ in range(4)]
  move_fishes(fish_table, smell_table, shark, moved_fish_table)

  # print('--fish move--')
  # for line in moved_fish_table:
  #   print([len(fishes) for fishes in line])

  move_shark(shark, moved_fish_table, smell_table)

  # print('--eaten move--')
  # for line in moved_fish_table:
  #   print([len(fishes) for fishes in line])

  remove_smell(smell_table)

  fish_table = moved_fish_table
  for y in range(4):
    for x in range(4):
      fish_table[y][x].extend(copied_fish_table[y][x])

  # print('----')
  # for line in fish_table:
  #   print([len(fishes) for fishes in line])
  # print('shark', shark.y, shark.x)

cnts = 0
for y in range(4):
  for x in range(4):
    cnts += len(fish_table[y][x])

print(cnts)