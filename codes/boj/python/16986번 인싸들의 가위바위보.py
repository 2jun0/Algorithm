import sys
def input(type=str):
  return type(sys.stdin.readline().strip())
def input_n(type=str):
  return list(map(type, input().split()))

class Battle:
  def __init__(self):
    self.p1, self.p2, self.other = 'A', 'B', 'C'
    self.a_idx, self.b_idx, self.c_idx = 0, 0, 0
    self.a_win_cnt, self.b_win_cnt, self.c_win_cnt = 0, 0, 0

  def is_end(self):
    return max(self.a_idx, self.b_idx, self.c_idx) >= 20 or max(self.a_win_cnt, self.b_win_cnt, self.c_win_cnt) >= K
  
  def copy(self):
    copied = Battle()

    copied.p1, copied.p2, copied.other = self.p1, self.p2, self.other
    copied.a_idx, copied.b_idx, copied.c_idx = self.a_idx, self.b_idx, self.c_idx
    copied.a_win_cnt, copied.b_win_cnt, copied.c_win_cnt = self.a_win_cnt, self.b_win_cnt, self.c_win_cnt
    
    return copied

  def play_turn(self):
    p1_choice = None
    p2_choice = None

    # p1, p2 패 선택
    if self.p1 == 'A':
      p1_choice = a_choices[self.a_idx]
      self.a_idx += 1
    elif self.p1 == 'B':
      p1_choice = b_choices[self.b_idx]
      self.b_idx += 1

    if self.p2 == 'B':
      p2_choice = b_choices[self.b_idx]
      self.b_idx += 1
    elif self.p2 == 'C':
      p2_choice = c_choices[self.c_idx]
      self.c_idx += 1

    # 우승자 선별 밑 플레이어 교체
    winner = None
    if A[p1_choice][p2_choice] == 2:
      # win p1
      winner, self.other, self.p2 = self.p1, self.p2, self.other
    else:
      # win p2
      winner, self.other, self.p1 = self.p2, self.p1, self.other
    
    # win count 증가
    if winner == 'A':
      self.a_win_cnt += 1
    elif winner == 'B':
      self.b_win_cnt += 1
    elif winner == 'C':
      self.c_win_cnt += 1

    self.p1, self.p2 = min(self.p1, self.p2), max(self.p1, self.p2)
      
def stack_a_choices_bfs(battle, visited):
  while battle.p1 != 'A' and not battle.is_end():
    battle.play_turn()

  if battle.is_end():
    return battle.a_win_cnt >= K

  for choice in range(0,N):
    if visited[choice]:
      continue

    a_choices[battle.a_idx] = choice
    visited[choice] = True
    new_battle = battle.copy()
    new_battle.play_turn()
    if stack_a_choices_bfs(new_battle, visited):
      return True
    visited[choice] = False
  return False

N, K = input_n(int)
A = [input_n(int) for _ in range(N)]

a_choices = [-1]*20
b_choices = input_n(int)
for b_idx in range(20):
  b_choices[b_idx] -= 1
c_choices = input_n(int)
for c_idx in range(20):
  c_choices[c_idx] -= 1

result = stack_a_choices_bfs(Battle(), [False]*N)

print(1 if result else 0)