import sys
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

class FireBall:
  def __init__(self, m, s, d):
    self.y = None
    self.x = None
    self.m = m
    self.s = s
    self.d = d
    
  def get_next_pos(self):
    assert self.y != None and self.x != None
    return dy[self.d]*self.s+self.y, dx[self.d]*self.s+self.x

def put_ball(table, ball, y, x):
  '''ball을 table의 y, x에 둔다.'''
  assert ball.y == None and ball.x == None

  ball.y, ball.x = y, x
  table[y][x].append(ball)

def remove_ball(table, ball):
  '''ball을 table에서 꺼낸다.'''
  assert ball.y != None and ball.x != None

  table[ball.y][ball.x].remove(ball)
  ball.y, ball.x = None, None

def move_ball(table, ball: FireBall):
  '''ball을 이동시킴'''
  nxt_y, nxt_x = ball.get_next_pos()
  nxt_y, nxt_x = nxt_y % N, nxt_x % N
  
  remove_ball(table, ball)
  put_ball(table, ball, nxt_y, nxt_x)

dy = [-1,-1,0,1,1,1,0,-1]
dx = [0,1,1,1,0,-1,-1,-1]

N, M, K = input_n(int)
table = [[[] for _ in range(N)] for _ in range(N)]

for _ in range(M):
  _y, _x, m, s, d = input_n(int)
  y, x = _y-1, _x-1
  put_ball(table, FireBall(m,s,d), y, x)

for _ in range(K):
  nxt_table = [[table[y][x][::] for x in range(N)] for y in range(N)]
  # 모든 파이어볼이 자신의 방향 di로 속력 si칸 만큼 이동한다.
  for y in range(N):
    for x in range(N):
      
      for ball in table[y][x]:
        move_ball(nxt_table, ball)

  table = nxt_table
  nxt_table = [[table[y][x][::] for x in range(N)] for y in range(N)]
  # 이동이 모두 끝난 뒤, 2개 이상의 파이어볼이 있는 칸에서는 다음과 같은 일이 일어난다
  for y in range(N):
    for x in range(N):
      if len(table[y][x]) >= 2:
        # 같은 칸에 있는 파이어볼은 모두 하나로 합쳐진다.
        sum_m = 0
        sum_s = 0
        is_every_d_even = True
        is_every_d_odd = True
        cnt = len(table[y][x])

        for ball in table[y][x]:
          sum_m += ball.m
          sum_s += ball.s
          if ball.d % 2 == 0:
            is_every_d_odd = False
          else:
            is_every_d_even = False

          remove_ball(nxt_table, ball)

        new_m = sum_m//5
        new_s = sum_s//cnt

        # 질량이 0인 파이어볼은 소멸되어 없어진다.
        # -> 생성하지 않는다.
        if new_m == 0:
          continue

        # 합쳐지는 파이어볼의 방향이 모두 홀수이거나 모두 짝수이면, 
        # 방향은 0, 2, 4, 6이 되고, 
        # 그렇지 않으면 1, 3, 5, 7이 된다.
        if is_every_d_even or is_every_d_odd:
          for new_d in [0,2,4,6]:
            put_ball(nxt_table, FireBall(new_m, new_s, new_d), y, x)
        else:
          for new_d in [1,3,5,7]:
            put_ball(nxt_table, FireBall(new_m, new_s, new_d), y, x)
  table = nxt_table
  
# for y in range(N):
#   print([[ball.m for ball in table[y][x]] for x in range(N)])

# 남아있는 파이어볼 질량의 합을 구해보자.
print(
  sum(
    sum(ball.m for ball in table[y][x])
  for x in range(N) for y in range(N))
)
