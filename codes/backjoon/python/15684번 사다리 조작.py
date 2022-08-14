from collections import deque
from copy import deepcopy
from itertools import combinations
import sys

def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

N, M, H = input_n(int)
has_lines = [[False]*(N-1) for _ in range(H)]
for _ in range(M):
  a, b = input_n(int)
  has_lines[a-1][b-1] = True

def can_add_lines(col, row_lines):
  can_add = True

  for row in row_lines:
    if has_lines[col][row]:
      can_add = False
    
  if can_add:
    for row in row_lines:
      has_lines[col][row] = True

    for row in row_lines:
      # check left
      if 0<=row-1 and has_lines[col][row-1]: can_add = False
      # check right
      if row+1<N-1 and has_lines[col][row+1]: can_add = False
    
    for row in row_lines:
      has_lines[col][row] = False
  
  return can_add

def bfs():
  costs = [{} for _ in range(H+1)]
  def set_costs(col, order, c):
    costs[col][tuple(order)] = c
  def get_costs(col, order):
    if tuple(order) not in costs[col]:
      return -1
    return costs[col][tuple(order)]

  q = deque()

  order = [row for row in range(N)]

  set_costs(0, order, 0)
  q.append((0, order))

  while q:
    col, order = q.popleft()
    cnt = get_costs(col, order)

    # print(col, order, cnt)

    if col == H:
      break

    order = deepcopy(order)

    for row in range(N-1):
      if has_lines[col][row]:
        order[row], order[row+1] = order[row+1], order[row]
      
    if get_costs(col+1, order) == -1:
      q.append((col+1, order))
      set_costs(col+1, order, cnt)
    elif get_costs(col+1, order) > cnt:
      set_costs(col+1, order, cnt)
    
    for add_cnt in range(1, 4):
      for row_lines in combinations([row for row in range(N-1)], add_cnt):
        if cnt+add_cnt > 3 or not can_add_lines(col, row_lines):
          continue

        n_order = deepcopy(order)

        for row in row_lines:
          n_order[row], n_order[row+1] = n_order[row+1], n_order[row]
            
        if get_costs(col+1, n_order) == -1:
          q.append((col+1, n_order))
          set_costs(col+1, n_order, cnt+add_cnt)
        elif get_costs(col+1, n_order) > cnt+add_cnt:
          set_costs(col+1, n_order, cnt+add_cnt)
 
  return get_costs(col, [row for row in range(N)])

print(bfs())