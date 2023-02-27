import sys
def input(type=str):
  return type(sys.stdin.readline().strip())
def input_n(type=str):
  return list(map(type, input().split()))

RIGHT = 1
LEFT = 2
UP = 3
DOWN = 4

WHITE = 0
RED = 1
BLUE = 2

def get_nxt_pos(y,x,d):
  nxt_y, nxt_x = y, x

  if d == LEFT:
    nxt_x = x - 1
  elif d == RIGHT:
    nxt_x = x + 1
  elif d == UP:
    nxt_y = y - 1
  elif d == DOWN:
    nxt_y = y + 1

  return nxt_y, nxt_x

def can_visit(y,x):
  '''방문할 수 있는가?'''
  return (0<=y<N and 0<=x<N) and table[y][x] != BLUE

class Piece:
  def __init__(self, y, x, d):
    self.y = y
    self.x = x
    self.d = d

  def move(self, _dont_reverse_d=False):
    '''말의 방향에 따라 자동으로 움직인다
    
    Args:
      _dont_reverse_d: 파란색 칸을 만났을 때, 2번 반복되는 것을 막는 플래그 변수

    Returns: 
      게임을 계속 이어 갈 수 있는지 여부
    '''
    nxt_y, nxt_x = get_nxt_pos(self.y, self.x, self.d)

    if can_visit(nxt_y, nxt_x):
      old_y, old_x = self.y, self.x

      if table[nxt_y][nxt_x] == WHITE:
        tmp_stack = []
        while True:
          p = stack_pieces[old_y][old_x].pop()
          tmp_stack.append(p)

          if p == self:
            break
        
        while tmp_stack:
          p = tmp_stack.pop()
          p.y, p.x = nxt_y, nxt_x
          stack_pieces[nxt_y][nxt_x].append(p)


      elif table[nxt_y][nxt_x] == RED:
        while True:
          p = stack_pieces[old_y][old_x].pop()
          p.y, p.x = nxt_y, nxt_x
          stack_pieces[nxt_y][nxt_x].append(p)

          if p == self:
            break
        
      return len(stack_pieces[nxt_y][nxt_x]) < 4
    elif not _dont_reverse_d:
      self.reverse_d()
      return self.move(_dont_reverse_d=True)
    else:
      return True

  def reverse_d(self):
    '''방향을 역으로 돌리는 함수'''
    if self.d == LEFT:
      self.d = RIGHT
    elif self.d == RIGHT:
      self.d = LEFT
    elif self.d == UP:
      self.d = DOWN
    elif self.d == DOWN:
      self.d = UP

N, K = input_n(int)
table = [input_n(int) for _ in range(N)]
stack_pieces = [[[] for _ in range(N)] for _ in range(N)]
pieces = []

for _ in range(K):
  y, x, d = input_n(int)
  y, x, = y - 1, x - 1
  p = Piece(y,x,d)
  pieces.append(p)
  stack_pieces[y][x].append(p)

turn = 0
end_flag = False
while turn <= 1000 and not end_flag:
  for p in pieces:
    if not p.move():
      end_flag = True
      break
  turn+=1

print(turn if turn <= 1000 else -1)