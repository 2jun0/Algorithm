from collections import defaultdict
import sys
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

def shift_down(table, tops):
  '''아래 한칸 지우면서 내림'''
  for y in range(1, 6):
    table[y-1] = table[y]
  table[5] = [0]*4

  # del 1
  for x in range(4):
    tops[x] = max(0, tops[x]-1)

def move_down(table, tops, remove_y):
  '''remove_y위에 있는 값들을 내림'''
  blocks_by_num = defaultdict(list)
  for x in range(4):
    for y in range(remove_y+1, 6):
      if table[y][x]:
        blocks_by_num[table[y][x]].append((y,x))

  # reset tops
  for x in range(4):
    tops[x] = 0
    for y in range(0, remove_y):
      if table[y][x]:
        tops[x] = max(tops[x], y+1)

  # 내려야 되는 것 내림
  moved = defaultdict(lambda: False)
  for y in range(remove_y+1, 6):
    for x in range(4):
      num = table[y][x]
      if num == 0 or moved[num]: continue
      
      moved[num] = True
      blocks = blocks_by_num[num]

      for by, bx in blocks:
        table[by][bx] = 0

      put(table, tops, blocks, num)

def put(table, tops, blocks, num):
  '''blocks을 table 위에 쌓음'''
  min_y = 0
  for _, x in blocks:
    min_y = max(min_y, tops[x])
  
  for _, x in blocks:
    y = max(min_y, tops[x])
    table[y][x] = num
    tops[x] = y+1

def next_table(table, tops):
  global score

  '''모든 행에 대해서 지울 수 있으면 지우기 (반복)'''
  while True:
    delete_y = -1
    for y in range(5, -1, -1):
      # 지워야 하는가?
      check = True
      for x in range(4):
        if table[y][x] == 0:
          # 하나라도 비워져있으면 지우지 말아야 함
          check = False
        
      if check:
        table[y] = [0]*4
        delete_y = max(delete_y, y)
        score += 1

    if delete_y != -1:
      move_down(table, tops, delete_y)
    else:
      break

  '''연한 칸에 블록이 있는 경우 shift'''
  while max(tops) > 4:
    shift_down(table, tops)

green = [[0] * 4 for _ in range(6)]
green_tops = [0]*4
blue = [[0] * 4 for _ in range(6)]
blue_tops = [0]*4
score = 0

N = input(int)
for num in range(1,N+1):
  t, x, y = input_n(int)

  if t == 1:
    put(green, green_tops, [(y,x)], num)
    put(blue, blue_tops, [(x,y)], num)
  elif t == 2:
    put(green, green_tops, [(y,x), (y+1, x)], num)
    put(blue, blue_tops, [(x,y), (x,y+1)], num)
  elif t == 3:
    put(green, green_tops, [(y,x), (y, x+1)], num)
    put(blue, blue_tops, [(x,y), (x+1,y)], num)

  next_table(green, green_tops)
  next_table(blue, blue_tops)

green_cnt = 0
for y in range(6):
  for x in range(4):
    if green[y][x]:
      green_cnt += 1
blue_cnt = 0
for y in range(6):
  for x in range(4):
    if blue[y][x]:
      blue_cnt += 1

print(score)
print(green_cnt+blue_cnt)
# print(green_cnt, blue_cnt)

# print('blue')
# for line in blue[::-1]:
#   print(line)

# print('tops',blue_tops)

# print('green')
# for line in green[::-1]:
#   print(line)

# print('tops',green_tops)