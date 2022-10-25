from collections import deque
import sys
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

INF = 10**8

class BlockGroup:
  def __init__(self, num):
    self.blocks = []
    self.std_pos = (INF, INF)
    self.rainbow_cnt = 0
    self.num = num

  def add_block(self, y, x, num):
    '''블럭 추가'''
    assert num in [self.num, 0]

    self.blocks.append((y,x))
    if self.num == num:
      self.std_pos = min(self.std_pos, (y,x))
    elif num == 0:
      self.rainbow_cnt += 1

  def get_sort_key(self):
    return (-len(self.blocks), -self.rainbow_cnt, -self.std_pos[0], -self.std_pos[1])

def get_block_groups(N, table, M):
  '''테이블의 블럭 그룹들을 반환'''
  def visit_block_group(sy, sx, visited):
    '''(sy, sx)기준으로 블럭 그룹을 찾음'''
    q = deque()

    visited[table[sy][sx]][sy][sx] = True
    q.append((sy,sx))

    block_group = BlockGroup(table[sy][sx])

    while q:
      y, x = q.popleft()
      block_group.add_block(y, x, table[y][x])

      for ny, nx in [(y+1, x), (y-1, x), (y, x+1), (y, x-1)]:
        if 0<=ny<N and 0<=nx<N and not visited[block_group.num][ny][nx] and table[ny][nx] in [0, block_group.num]:
          visited[block_group.num][ny][nx] = True
          q.append((ny,nx))

    if len(block_group.blocks) >= 2:
      return block_group
    else:
      return None

  block_groups = []
  visited = [[[False]*N for _ in range(N)] for _ in range(M+1)]

  for y in range(N):
    for x in range(N):
      if table[y][x] not in [-1, 0, None] and not visited[table[y][x]][y][x]:
        block_group = visit_block_group(y, x, visited)
        if block_group:
          block_groups.append(block_group)

  return block_groups

def pop_block_group(table, block_group):
  '''블럭 그룹에 있는 블럭들을 모두 제거
  - 점수 반환
  '''
  score = len(block_group.blocks)**2
  for y, x in block_group.blocks:
    table[y][x] = None

  return score

def fall_down(N, table):
  '''중력이 작용함'''
  for x in range(N):
    top = N-1
    
    for y in range(N-1, -1, -1):
      # top 찾기
      if table[y][x] == -1:
        top = y
      while top > y and table[top][x] != None:
        top -= 1

      if top >= 0 and table[top][x] == None:
        table[top][x], table[y][x] = table[y][x], table[top][x]

def turn_left(N, table):
  '''90도 반시계 방향으로 회전한다'''
  new_table = [[None]*N for _ in range(N)]
  for y in range(N):
    for x in range(N):
      new_table[N-1-x][y] = table[y][x]

  for y in range(N):
    for x in range(N):
      table[y][x] = new_table[y][x]

def play(N, table, M):
  score = 0

  while True:
    block_groups = get_block_groups(N, table, M)
    if not block_groups:
      break

    block_groups.sort(key=lambda bg: bg.get_sort_key())
    score += pop_block_group(table, block_groups[0])
    fall_down(N, table)
    turn_left(N, table)
    fall_down(N, table)

  return score


N, M  = input_n(int)
table = [input_n(int) for _ in range(N)]
print(play(N, table, M))
