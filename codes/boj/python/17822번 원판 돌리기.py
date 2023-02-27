import sys
def input(type=str):
  return type(sys.stdin.readline().strip())
def input_n(type=str):
  return list(map(type, input().split()))

RIGHT = 0
LEFT = 1

def turn(x, d, k):
  '''원판 돌리기'''
  global circle

  for xi in range(x-1, N, x):
    if d == LEFT:
      circle[xi] = circle[xi][k:] + circle[xi][:k]
    elif d == RIGHT:
      circle[xi] = circle[xi][-k:] + circle[xi][:-k]
  
  if not remove_adj_same_nums():
    update_circle()

def update_circle():
  '''인접 수가 같은 것 없는 경우'''
  if remaining_cnt == 0:
    return

  avg = sum([sum(c) for c in circle]) / remaining_cnt
  for xi in range(N):
    # ling index
    for ci in range(M):
      # ling el index
      if circle[xi][ci] == 0:
        continue

      if circle[xi][ci] > avg:
        circle[xi][ci] -= 1
      elif circle[xi][ci] < avg:
        circle[xi][ci] += 1

def remove_adj_same_nums():
  '''인접 수가 같은 것 지우기'''
  global remaining_cnt 
  have_adj_sames = [[False]*M for _ in range(N)]

  '''have_adj_sames를 이용해 구분'''
  for xi in range(N):
    # ling index
    for ci in range(M):
      # ling el index

      if circle[xi][ci] == 0:
        continue

      flag = False
      for adj_xi, adj_ci in [(xi, (ci-1)%M), (xi, (ci+1)%M), (xi+1, ci), (xi-1, ci)]:
        # left, right, up, down
        if (0<=adj_xi<N and 0<=adj_ci<M) and circle[xi][ci] == circle[adj_xi][adj_ci]:
          flag = True
          have_adj_sames[adj_xi][adj_ci] = True
      
      if flag:
        have_adj_sames[xi][ci] = True

  '''have_adj_sames를 통해 circle 수정'''
  for xi in range(N):
    # ling index
    for ci in range(M):
      # ling el index

      if have_adj_sames[xi][ci] and circle[xi][ci] != 0:
        circle[xi][ci] = 0
        remaining_cnt -= 1

  return sum([sum(L) for L in have_adj_sames]) and True

N, M, T = input_n(int)
circle = [input_n(int) for _ in range(N)]
remaining_cnt = N*M

for _ in range(T):
  x, d, k = input_n(int)
  turn(x,d,k)

print(sum([sum(c) for c in circle]))