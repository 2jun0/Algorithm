from collections import deque
from itertools import combinations
import sys
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
  return list(map(_type, input().split()))

def get_rest_of_combinations(populations, combi_cases):
  rest = []
  for case in combi_cases:
    rest_by_case = populations.copy()
    for elm in case:
      rest_by_case.remove(elm)
    rest.append(rest_by_case)
  return rest

def cultivate_bfs(green_start_pos_list, red_start_pos_list):
  dists_green = [[-1]*M for _ in range(N)]
  dists_red = [[-1]*M for _ in range(N)]
  meeted = [[False]*M for _ in range(N)]

  meet_cnt = 0

  # init dists and queues
  q = deque()
  for y, x in green_start_pos_list:
    dists_green[y][x] = 0
    q.append((y,x,'green'))
  for y, x in red_start_pos_list:
    dists_red[y][x] = 0
    q.append((y,x,'red'))

  # 배양액이 만나는 지점 찾기
  while q:
    y, x, color = q.popleft()

    # 또 만나는 걸 방지하기 위함.
    if meeted[y][x]:
      continue

    # 배양액이 만남
    if dists_green[y][x] != -1 and dists_red[y][x] != -1 and dists_green[y][x] == dists_red[y][x]:
      meeted[y][x] = True
      meet_cnt += 1
      continue
  
    for n_y, n_x in [(y+1, x),(y-1, x),(y, x+1),(y, x-1)]:
      if 0<=n_y<N and 0<=n_x<M and table[n_y][n_x] != 0:
        if color == 'green' and dists_green[n_y][n_x] == -1:
          dists_green[n_y][n_x] = dists_green[y][x] + 1
          q.append((n_y, n_x, 'green'))
        elif color == 'red' and dists_red[n_y][n_x] == -1:
          dists_red[n_y][n_x] = dists_red[y][x] + 1
          q.append((n_y, n_x, 'red'))
  
  return meet_cnt

N, M, G, R = input_n(int)
table = [input_n(int) for _ in range(N)]

start_pos_populations = []
for y in range(N):
  for x in range(M):
    if table[y][x] == 2:
      start_pos_populations.append((y,x))

max_meet_cnt = 0
for start_pos_list in combinations(start_pos_populations, G+R):
  start_pos_list = list(start_pos_list)
  green_start_pos_cases = list(combinations(start_pos_list, G))
  red_start_pos_cases = get_rest_of_combinations(start_pos_list, green_start_pos_cases)

  for green_start_pos_list, red_start_pos_list in zip(green_start_pos_cases, red_start_pos_cases):
    max_meet_cnt = max(max_meet_cnt, cultivate_bfs(green_start_pos_list, red_start_pos_list))

print(max_meet_cnt)