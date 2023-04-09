import sys

def input(type_=str):
	return type_(sys.stdin.readline().rstrip())
def input_n(type_):
	return list(map(type_, input().split()))

INF = 50

def get_food_lr(left = True):
  if left:
    tar_x = g_srt[0]-1
  else:
    tar_x = g_end[0]+1
  
  if tar_x < 0 or tar_x >= N:
    return -INF
  
  sum_ = 0
  for y in range(g_srt[1], g_end[1]+1):
    sum_ += table[y][tar_x]
  return sum_

def get_food_ud(up = True):
  if up:
    tar_y = g_srt[1]-1
  else:
    tar_y = g_end[1]+1
  
  if tar_y < 0 or tar_y >= N:
    return -INF
  
  sum_ = 0
  for x in range(g_srt[0], g_end[0]+1):
    sum_ += table[tar_y][x]
  return sum_

N = input(int)
table = [input_n(int) for _ in range(N)]

g_srt = [N//2-1, N//2-1]
g_end = [N//2, N//2]
food = 0
log = ''

while True:
  lf = get_food_lr(True)
  rf = get_food_lr(False)
  uf = get_food_ud(True)
  df = get_food_ud(False)
  
  max_f = max(lf, rf, uf, df)
  # print(uf, df, lf, rf)
  if max_f <= 0:
    break
  
  if uf == max_f:
    food += uf
    g_srt[1] -= 1
    log += 'U'
  elif df == max_f:
    food += df
    g_end[1] += 1
    log += 'D'
  elif lf == max_f:
    food += lf
    g_srt[0] -= 1
    log += 'L'
  elif rf == max_f:
    food += rf
    g_end[0] += 1
    log += 'R'
    
print(food)
print(log)