from copy import deepcopy
import sys
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

dy = [-1,1,0,0]
dx = [0,0,-1,1]

class Shark: 
  def __init__(self, y, x, num):
    self.y = y
    self.x = x
    self.num = num
  
  def set_priority(self, priority):
    self.priority = priority

  def set_d(self, d):
    self.d = d
  
  def move(self, table, nxt_table):
    '''상어 움직이기'''
    
    nxt_y, nxt_x, nxt_d = self._get_next_pos(table)

    if K-1 > 0:
      nxt_table[self.y][self.x] = Smell(self.y, self.x, self)
    self.d = nxt_d

    if isinstance(nxt_table[nxt_y][nxt_x], Shark):
      # 다른 상어가 있으면 숫자 비교 (내가 작으면 나로 변경, 그게 아니면 패스)
      other: Shark = nxt_table[nxt_y][nxt_x]
      if self.num < other.num:
        nxt_table[nxt_y][nxt_x] = self
    else:
      nxt_table[nxt_y][nxt_x] = self
    
    self.y, self.x = nxt_y, nxt_x

  def _get_next_pos(self, table):
    '''움직일 다음 좌표 구하기'''

    # 갈 수 있는 모든 경우의 수
    cases = [(self.y+dy[d], self.x+dx[d], d) for d in self.priority[self.d]]

    # 범위 벗어난 케이스 제거
    cases = list(filter(lambda yxd: 0<=yxd[0]<N and 0<=yxd[1]<N, cases))

    # 움직임의 우선순위
    # 0 : 빈칸
    # 1 : 내 냄새
    # 2 : 나머지 (상어, 다른 상어 냄새)
    cases.sort(key = lambda yxd: (
      0 if table[yxd[0]][yxd[1]] == None  
      else
      1 if isinstance(table[yxd[0]][yxd[1]], Smell) and table[yxd[0]][yxd[1]].owner == self
      else 
      2
    ))

    return cases[0]

class Smell:
  def __init__(self, y, x, owner):
    self.y = y
    self.x = x
    self.owner = owner
    self.remain = K-1

  def next_turn(self, nxt_table):
    '''다음 턴 -> 냄새 향이 약해짐'''

    # 더 이상 진행할 수 없음
    assert self.remain > 0

    self.remain -= 1
    
    if self.remain == 0:
      # 냄새가 다 빠지면 없는 걸로 처리
      nxt_table[self.y][self.x] = None

def play():
  global table

  move_cnt = 0
  while True:
  # for _ in range(5):
    sharks = []
    smells = []
    for y in range(N):
      for x in range(N):
        if isinstance(table[y][x], Shark):
          sharks.append(table[y][x])
        elif isinstance(table[y][x], Smell):
          smells.append(table[y][x])
      
    if len(sharks) == 1:
      break

    move_cnt += 1
    nxt_table = [[table[y][x] for x in range(N)] for y in range(N)]

    # 냄새
    for smell in smells:
      smell.next_turn(nxt_table)

    # 상어
    for shark in sharks:
      shark.move(table, nxt_table)

    table = nxt_table

    if move_cnt > 1000:
      return -1

  return move_cnt

N, M, K = input_n(int)
table = [input_n(int) for _ in range(N)]
sharks = [None]*M

for y in range(N):
  for x in range(N):
    if table[y][x] == 0:
      table[y][x] = None
    else:
      num = table[y][x]-1
      shark = Shark(y, x, num)
      table[y][x] = shark
      sharks[num] = shark

for d, shark in zip(input_n(int), sharks):
  shark.set_d(d-1)

for shark in sharks:
  
  # base_d 기준 우선순위 d
  priority = [None]*4
  for base_d in range(4):
    priority[base_d] = [d-1 for d in input_n(int)]
  shark.set_priority(priority)

print(play())

# for y in range(N):
#   print(['s'+str(x.remain) if isinstance(x, Smell) else 'S' if isinstance(x, Shark) else None for x in table[y]])