import sys
INF = 10**10
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))
def print_n(L, join_str=' '):
  for i,l in enumerate(L): print(l, end=join_str if i<len(L)-1 else '\n')
def LL(n,m,d=0): return [[d]*n for _ in range(m)]
def avg(l): return sum(l)/len(l)

UP, DOWN, RIGHT, LEFT = 1, 2, 3, 4

R, C, M = input_n(int)

class Shark:
  def __init__(self, v):
    self.idx = 0
    self.is_live = True
    self.r = v[0]-1
    self.c = v[1]-1
    self.s = v[2]
    self.d = v[3]
    self.z = v[4]

    if self.d == LEFT and self.c == 0: self.d = RIGHT
    if self.d == RIGHT and self.c == C-1: self.d = LEFT
    if self.d == UP and self.r == 0: self.d = DOWN
    if self.d == DOWN and self.r == R-1: self.d = UP



S = [Shark(input_n(int)) for _ in range(M)]

table = [[None]*C for _ in range(R)]
for s in S: table[s.r][s.c] = s

sum_z = 0
for pc in range(C):
  # 낚았다!
  for pr in range(R):
    if table[pr][pc]:
      sum_z += table[pr][pc].z
      table[pr][pc].is_live = False
      table[pr][pc] = None

      break
  # 움직였다!
  for s in S:
    if not s.is_live: continue

    if table[s.r][s.c] == s: 
      table[s.r][s.c] = None
    s.idx += 1
    if s.d in [LEFT, RIGHT]:
      if s.d == RIGHT: c = s.c
      else: c = 2*(C-1)-s.c
      c=(c+s.s)%(2*(C-1))

      if c < C-1:
        s.d = RIGHT
        s.c = c
      else:
        s.d = LEFT
        s.c = 2*(C-1)-c
    if s.d in [UP, DOWN]:
      if s.d == DOWN: r = s.r
      else: r = 2*(R-1)-s.r
      r=(r+s.s)%(2*(R-1))

      if r < R-1:
        s.d = DOWN
        s.r = r
      else:
        s.d = UP
        s.r = 2*(R-1)-r

    # 상어 인카운트
    if table[s.r][s.c] and table[s.r][s.c].idx == s.idx:
      # 내가 먹음
      if table[s.r][s.c].z < s.z:
        table[s.r][s.c].is_live = False
        table[s.r][s.c] = s
      # 내가 먹힘
      else:
        s.is_live = False
    else:
      table[s.r][s.c] = s
    
print(sum_z)
    