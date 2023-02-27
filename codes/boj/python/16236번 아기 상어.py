import sys
sys.setrecursionlimit(100000) # 재귀 제한 풀기

import heapq

# custom heap
class CustomHeap:
  class Node(object):
    def __init__(self, val, comparator=None):
      self.val = val
      self.comparator = comparator

    def __repr__(self):
      return f'Node value: {self.val}'

    def __lt__(self, other):
      if self.comparator:
        return self.comparator(self.val, other.val)
      else:
        return self.val < other.val

  def __init__(self, comparator=None):
    self.heap = []
    self.comparator = comparator

  def push(self, val):
    heapq.heappush(self.heap, CustomHeap.Node(val, self.comparator))

  def pop(self):
    return heapq.heappop(self.heap).val

  def is_empty(self):
    return len(self.heap) == 0
##

def _input():
  return sys.stdin.readline().rstrip()
def _input_n(_type):
  return map(_type, _input().split())

def node_comparator(val1, val2):
  if val1[2] != val2[2]: # dist
    return val1[2] < val2[2]
  elif val1[1] != val2[1]: # y
    return val1[1] < val2[1]
  elif val1[0] != val2[0]: # x
    return val1[0] < val2[0]
  else:
    return True


def find(field, shark_size, shark_pos):

  def dequeue(x,y,cur_dist):
    check.dist_field[y][x] = cur_dist
    check.queue.push((x,y,cur_dist))

  def enqueue_neighbor(x,y,cur_dist):
    nebors_pos = [{'x':x, 'y':y-1}, {'x':x-1, 'y':y}, {'x':x+1, 'y':y}, {'x':x, 'y':y+1}]
    for nebor_pos in nebors_pos:
      if nebor_pos['y'] < 0 or nebor_pos['y'] >= len(check.dist_field):
        continue

      if nebor_pos['x'] < 0 or nebor_pos['x'] >= len(check.dist_field):
        continue

      if check.dist_field[nebor_pos['y']][nebor_pos['x']] != 0: # 이미 탐색함
        continue

      dequeue(x=nebor_pos['x'],y=nebor_pos['y'],cur_dist=cur_dist+1)

  def check(x,y,field): # return eatable, sizeOfFish
    cur_dist = check.dist_field[y][x]

    if field[y][x] > shark_size: # too big to eat
      return False, field[y][x]
    elif field[y][x] < shark_size and field[y][x] > 0: # eatable
      return True, field[y][x]
    else: # 못먹고 가는 경우
      enqueue_neighbor(x,y,cur_dist)
      return False, 0

  def next():
    x,y,cur_dist = check.queue.pop()
    eatable, fish_size = check(x,y,field)
    return x, y, eatable, fish_size

  # init dist_field
  check.dist_field = [[0]*len(field) for _ in range(len(field))]
  check.dist_field[shark_pos['y']][shark_pos['x']] = -1 # 상어는 -1로 한다. (탐색 제외)
  check.queue = CustomHeap(comparator=node_comparator)

  enqueue_neighbor(shark_pos['x'], shark_pos['y'], cur_dist=0)
  while not check.queue.is_empty():
    x, y, eatable, fish_size = next()
    if eatable:
      return x, y, fish_size, check.dist_field[y][x]

  return -1, -1, -1, -1


def act():
  N = int(_input())
  field = []
  shark_size = 2
  shark_pos = {'x':0, 'y':0}
  fish_cnt = 0

  # field mapping
  for y in range(N):
    line = list(_input_n(int))
    for x in range(N):
      if line[x] == 9:
        shark_pos['x'] = x
        shark_pos['y'] = y
      elif line[x] != 0:
        fish_cnt += 1
    field.append(line)

  movement = 0
  eat_cnt = 0
  for _ in range(fish_cnt):
    x,y,fish_size,dist = find(field, shark_size, shark_pos)
    if dist == -1:
      break

    field[y][x] = 9
    field[shark_pos['y']][shark_pos['x']] = 0
    shark_pos['y'] = y
    shark_pos['x'] = x
    eat_cnt += 1
    if shark_size == eat_cnt:
      shark_size += 1
      eat_cnt = 0
    movement += dist
    
  
  print(movement)

act()