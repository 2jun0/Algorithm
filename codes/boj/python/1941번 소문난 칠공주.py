from collections import deque
from itertools import combinations
import sys
def input(_type=str):
	return _type(sys.stdin.readline().strip())

table = [input(str) for _ in range(5)]

def check_case(case):
  visited = [[False]*5 for _ in range(5)]
  is_in_case = [[False]*5 for _ in range(5)]
  
  for y, x in case:
    is_in_case[y][x] = True

  q = deque([case[0]])
  visited[case[0][0]][case[0][1]] = True

  cnt = 0
  s_cnt = 0
  while q:
    y, x = q.popleft()
    cnt += 1
    if table[y][x] == 'S':
      s_cnt += 1

    for n_y, n_x in [(y+1, x),(y-1, x),(y, x+1),(y, x-1)]:
      if 0<=n_y<5 and 0<=n_x<5:
        if is_in_case[n_y][n_x] and not visited[n_y][n_x]:
          visited[n_y][n_x] = True
          q.append((n_y, n_x))

  if cnt == 7 and s_cnt >= 4:
    return True

  return False

population = [(y,x) for y in range(5) for x in range(5)]
all_cases = list(combinations(population, 7))

case_cnt = 0
for case in all_cases:
  if check_case(case):
    case_cnt += 1 

print(case_cnt)