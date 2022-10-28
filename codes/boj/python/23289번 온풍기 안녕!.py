from collections import deque
from copy import deepcopy
import sys
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

LEFT, DOWN, RIGHT, UP = 0, 1, 2, 3
dy = [0, 1, 0, -1]
dx = [-1, 0, 1, 0]

def check_range(R, C, y, x):
  '''범위 확인 함수'''
  return 0<=y<R and 0<=x<C

def blow(R, C, table, has_wall, sy, sx, d):
  '''온풍기에서 바람이 나옴'''
  add_table = [[0]*C for _ in range(R)]
  q = deque()

  add_table[sy+dy[d]][sx+dx[d]] = 5
  q.append((sy+dy[d],sx+dx[d]))

  while q:
    y, x = q.popleft()

    if add_table[y][x] == 1:
      continue

    nxt_poses = []
    # 앞
    if not has_wall[y][x][d]:
      ny, nx = y+dy[d], x+dx[d]
      if check_range(R, C, ny, nx):
        nxt_poses.append((ny, nx))
    # 왼쪽 앞
    nd = (d+1)%4
    if not has_wall[y][x][nd]:
      ly, lx = y+dy[nd], x+dx[nd]
      if check_range(R, C, ly, lx) and not has_wall[ly][lx][d]:
        ny, nx = ly+dy[d], lx+dx[d]
        if check_range(R, C, ny, nx):
          # 벽 검사를 한번 더 해야함
          nxt_poses.append((ny, nx))
    # 오른쪽 앞
    nd = (d-1)%4
    if not has_wall[y][x][nd]:
      ry, rx = y+dy[nd], x+dx[nd]
      if check_range(R, C, ry, rx) and not has_wall[ry][rx][d]:
        ny, nx = ry+dy[d], rx+dx[d]
        if check_range(R, C, ny, nx):
          # 벽 검사를 한번 더 해야함
          nxt_poses.append((ny, nx))

    for ny, nx in nxt_poses:
      if 0<=ny<R and 0<=nx<C and add_table[ny][nx] == 0:
        add_table[ny][nx] = add_table[y][x] - 1
        q.append((ny,nx))

  for y in range(R):
    for x in range(C):
      table[y][x] += add_table[y][x]

def update_temperature(R, C, table, has_wall):
  '''온도가 조절됨'''
  new_table = deepcopy(table)

  for y in range(R):
    for x in range(C):
      if table[y][x] <= 0:
        continue

      for d in range(4):
        if has_wall[y][x][d]:
          # 벽이 없어야 함
          continue

        adjy, adjx = y+dy[d], x+dx[d]

        if not check_range(R, C, adjy, adjx) or table[adjy][adjx] >= table[y][x]:
          # 인접한 온도가 낮아야 함
          continue

        diff = table[y][x] - table[adjy][adjx]
        new_table[adjy][adjx] += diff // 4
        new_table[y][x] -= diff // 4

  for y in range(R):
    for x in range(C):
      table[y][x] = new_table[y][x]

def decrease_outer(R, C, table):
  '''바깥쪽 칸 온도 감소'''
  for y in range(R):
    table[y][0] = max(0, table[y][0]-1)
    table[y][-1] = max(0, table[y][-1]-1)
  
  for x in range(1,C-1):
    table[0][x] = max(0, table[0][x]-1)
    table[-1][x] = max(0, table[-1][x]-1)


R, C, K = input_n(int)
table = [input_n(int) for _ in range(R)]
machines = []
check_poses = []

for y in range(R):
  for x in range(C):
    if table[y][x] == 1:
      machines.append((y,x,RIGHT))
    elif table[y][x] == 2:
      machines.append((y,x,LEFT))
    elif table[y][x] == 3:
      machines.append((y,x,UP))
    elif table[y][x] == 4:
      machines.append((y,x,DOWN))
    elif table[y][x] == 5:
      check_poses.append((y,x))
    table[y][x] = 0

W = input(int)
has_wall = [[[False]*4 for _ in range(C)] for _ in range(R)]
for _ in range(W):
  _y, _x, t = input_n(int)
  y, x = _y-1, _x-1
  if t == 0:
    for adjy, adjx, d in [(y-1,x,DOWN), (y,x,UP)]:
      if check_range(R, C, adjy, adjx):
        has_wall[adjy][adjx][d] = True
  elif t == 1:
    for adjy, adjx, d in [(y,x,RIGHT), (y,x+1,LEFT)]:
      if check_range(R, C, adjy, adjx):
        has_wall[adjy][adjx][d] = True

turn = 0
while True:
  for my, mx, md in machines:
    blow(R, C, table, has_wall, my, mx, md)

  update_temperature(R, C, table, has_wall)
  decrease_outer(R, C, table)

  turn += 1

  flag = True
  for y, x in check_poses:
    if table[y][x] < K:
      flag = False

  if flag or turn > 100:
    break

print(turn)