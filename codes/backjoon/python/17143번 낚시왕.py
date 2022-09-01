import sys
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

UP, DOWN, RIGHT, LEFT = 1, 2, 3, 4

class Shark:
  def __init__(self, y, x, speed, d, size):
    self.is_live = True

    self.y = y
    self.x = x
    self.speed = speed
    self.d = d
    self.size = size

  def move(self):
    if self.d == LEFT:
      self.x -= self.speed
    elif self.d == RIGHT:
      self.x += self.speed
    elif self.d == UP:
      self.y -= self.speed
    elif self.d == DOWN:
      self.y += self.speed

    while True:
      if self.x < 0:
        self.x = 0 + (0 - self.x)
        self.d = RIGHT  
      elif self.x >= C:
        self.x = (C-1) - (self.x - (C-1))
        self.d = LEFT
      elif self.y < 0:
        self.y = 0 + (0 - self.y)
        self.d = DOWN
      elif self.y >= R:
        self.y = (R-1) - (self.y - (R-1))
        self.d = UP
      else:
        break
      

R, C, M = input_n(int)
table = [[None]*C for _ in range(R)]
nxt_table = [[None]*C for _ in range(R)]
S = []

for _ in range(M):
  y, x, s, d, z = input_n(int)
  y, x = y-1, x-1

  s = Shark(y,x,s,d,z)
  S.append(s)
  table[y][x] = s

sum_z = 0
for px in range(C):
  # 낚았다!
  for py in range(R):
    if table[py][px]:
      sum_z += table[py][px].size
      table[py][px].is_live = False
      table[py][px] = None
      break

  # 움직였다!
  for s in S:
    # 죽은 경우 제외
    if not s.is_live: continue 

    table[s.y][s.x] = None
    
    s.move()

    # 상어 인카운트 시
    if nxt_table[s.y][s.x]:
      other = nxt_table[s.y][s.x]
      
      if s.size > other.size:
        # 내가 먹음
        other.is_live = False
        nxt_table[s.y][s.x] = s
      else:
        # 내가 먹힘
        s.is_live = False
    else:
      nxt_table[s.y][s.x] = s
  
  table, nxt_table = nxt_table, table
    
print(sum_z)
    