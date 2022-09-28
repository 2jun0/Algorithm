import sys
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

d2dy = [-1,-1,0,1,1,1,0,-1]
d2dx = [0,-1,-1,-1,0,1,1,1]

class Shark:
  def __init__(self, table, y, x, d, v):
    self.table = table
    self.y = y
    self.x = x
    self.d = d
    self.v = v
    self.last_victim = None
    self.prev_status = [] 
    '''y, x, d, v, last_victim'''
  
  def get_move_cases(self):
    # 갈 수 있는 y, x
    move_cases = []
    
    nxt_y = self.y + d2dy[self.d]
    nxt_x = self.x + d2dx[self.d]
    while 0<=nxt_y<4 and 0<=nxt_x<4:
      if self.table[nxt_y][nxt_x]:
        # 뭔가 있으면 움직일 수 있음 (물고기 임)
        move_cases.append((nxt_y, nxt_x))

      nxt_y += d2dy[self.d]
      nxt_x += d2dx[self.d]

    return move_cases

  def move(self, nxt_y, nxt_x):
    '''nxt_y, nxt_x로 이동'''

    # ASSERT 오류 방지용 -> 뭔가 있어야 함 (물고기일 것임)
    assert self.table[nxt_y][nxt_x] != None

    # save prev status
    self.prev_status.append((self.y, self.x, self.d, self.v, self.last_victim))

    # nxt_last_victim, nxt_v
    nxt_last_victim = self.table[nxt_y][nxt_x]
    nxt_v = self.v + nxt_last_victim.v
    nxt_d = nxt_last_victim.d
    nxt_last_victim.is_dead = True

    # 이동
    self.table[self.y][self.x] = None
    self.table[nxt_y][nxt_x] = self
    
    # nxt status
    self.y, self.x, self.d, self.v, self.last_victim = nxt_y, nxt_x, nxt_d, nxt_v, nxt_last_victim

  def rollback(self):
    '''한번 뒤로 돌아감'''
    prev_y, prev_x, prev_d, prev_v, prev_last_victim = self.prev_status.pop()

    # ASSERT 오류 방지용 -> 뭔가 없어야 함
    assert self.table[prev_y][prev_x] == None

    # 뒤로 이동
    self.table[prev_y][prev_x] = self

    # 현재 먹었던 물고기 뱉음
    self.table[self.y][self.x] = self.last_victim
    self.last_victim.is_dead = False

    # rollback status
    self.y, self.x, self.d, self.v, self.last_victim = prev_y, prev_x, prev_d, prev_v, prev_last_victim

class Fish:
  def __init__(self, table, y, x, d, v):
    self.table = table
    self.y = y
    self.x = x
    self.d = d
    self.v = v
    self.is_dead = False
    self.prev_status = []
    '''y, x, d'''

  def move(self):
    '''움직일 수 있으면 움직이기
    @Return: 움직임 여부
    '''
    # save prev_status
    self.prev_status.append((self.y, self.x, self.d))

    if self.is_dead:
      return False

    # nxt_d
    nxt_d = self.get_nxt_d()

    if nxt_d == -1:
      return False

    # nxt_y, nxt_x
    nxt_y = self.y + d2dy[nxt_d]
    nxt_x = self.x + d2dx[nxt_d]

    # swap
    if self.table[nxt_y][nxt_x] == None:
      self.table[self.y][self.x], self.table[nxt_y][nxt_x] = None, self
    else:
      other = self.table[nxt_y][nxt_x]
      self.table[self.y][self.x], self.table[nxt_y][nxt_x] = other, self
      other.y, other.x = self.y, self.x
    
    # nxt status
    self.y, self.x, self.d = nxt_y, nxt_x, nxt_d

    return True
  
  def get_nxt_d(self):
    '''다음으로 움직여야 할 d를 구함
    - 아예 움직일 수 없으면 -1
    '''
    for nxt_d in [(self.d+dd)%8 for dd in range(8)]:
      # nxt_d: 움직일 수 있을 때 까지 시계 반대방향으로 돌음
      nxt_y = self.y + d2dy[nxt_d]
      nxt_x = self.x + d2dx[nxt_d]

      if not (0<=nxt_y<4 and 0<=nxt_x<4):
        # 범위를 벗어남
        continue
      if isinstance(self.table[nxt_y][nxt_x], Shark):
        # 상어가 있는 곳은 갈 수 없음
        continue

      return nxt_d
    
    return -1

  def rollback(self):
    '''뒤로 이동'''
    prev_y, prev_x, prev_d = self.prev_status.pop()

    if (prev_y, prev_x, prev_d) == (self.y, self.x, self.d):
      # 아무변화가 없었음 -> 이동을 안했다
      return

    # swap
    if self.table[prev_y][prev_x] == None:
      self.table[self.y][self.x], self.table[prev_y][prev_x] = None, self
    else:
      assert not isinstance(self.table[prev_y][prev_x], Shark)
      other = self.table[prev_y][prev_x]
      self.table[self.y][self.x], self.table[prev_y][prev_x] = other, self
      other.y, other.x = self.y, self.x

    # rollback status
    self.y, self.x, self.d = prev_y, prev_x, prev_d


def get_max_shark_v_dfs(shark: Shark, fishes):
  '''dfs로 상어의 최대 v를 찾음'''
  global max_shark_v

  for idx in range(len(fishes)):
    fishes[idx].move()

  move_cases = shark.get_move_cases()
  # print('Shark' , (shark.y, shark.x), shark.d, shark.v)
  # print(move_cases)

  if len(move_cases) > 0:
    for nxt_y, nxt_x in move_cases:
      shark.move(nxt_y, nxt_x)
      get_max_shark_v_dfs(shark, fishes)
      shark.rollback()
  else:
    max_shark_v = max(max_shark_v, shark.v)

  for idx in range(len(fishes)-1, -1, -1):
    fishes[idx].rollback()

table = [[None]*4 for _ in range(4)]
fishes = []
shark = None
max_shark_v = 0

for y in range(4):
  inputs = input_n(int)
  for x in range(4):
    v = inputs[x*2]
    d = inputs[x*2+1] - 1

    fish = Fish(table, y, x, d, v)

    fishes.append(fish)
    table[y][x] = fish

fishes.sort(key=lambda fish : fish.v)

# 맨 처음 상어 0,0 으로 이동
shark = Shark(table, 0, 0, table[0][0].d, table[0][0].v)
shark.last_victim = table[0][0]
shark.last_victim.is_dead = True
table[0][0] = shark

get_max_shark_v_dfs(shark, fishes)
print(max_shark_v)