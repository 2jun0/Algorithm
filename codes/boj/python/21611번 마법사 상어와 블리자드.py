import sys
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

dy = [0, 1, 0, -1]
dx = [-1, 0, 1, 0]

def get_edges(N):
  '''꼭짓점 구하기'''
  edge_nums = [1, 2]
  while edge_nums[-1] < N*N:
    diff = edge_nums[-1] - edge_nums[-2] + 1
    edge_nums.append(edge_nums[-1] + diff)
    edge_nums.append(edge_nums[-1] + diff)

  edges = []
  y, x = N//2, N//2
  d = 0
  idx = 0
  while 0<=y<N and 0<=x<N:
    diff = edge_nums[idx+1] - edge_nums[idx]
    for _ in range(2):
      y += dy[d] * diff
      x += dx[d] * diff
      if 0<=y<N and 0<=x<N:
        edges.append((y,x))
      d = (d+1)%4
    idx += 2

  return edges

def get_line(N, table):
  '''테이블을 길게 늘이기'''
  edges = get_edges(N)
  line = []

  d = 0
  y, x = N//2, N//2-1

  while 0<=y<N and 0<=x<N:
    line.append(table[y][x])

    if (y, x) in edges:
      d = (d+1) % 4
    y += dy[d]
    x += dx[d]

  return line

def move_center(line):
  '''블럭들이 가운데로 이동'''
  new_line = []
  for num in line:
    if num != 0:
      new_line.append(num)
  
  return new_line

def get_groups(line):
  '''블럭을 그룹화 함'''
  groups = []
  last_num = -1
  for idx, num in enumerate(line):
    if num == 0:
      continue

    if last_num != num:
      groups.append([])
      last_num = num

    groups[-1].append(idx)
  return groups

def pop_blocks(line):
  '''4개이상 모여있는 블럭 폭발'''
  poped_cnts = [0,0,0]
  
  groups = get_groups(line)
  for group in groups:
    if len(group) >= 4:
      for idx in group:
        poped_cnts[line[idx]-1] += 1
        line[idx] = 0

  return poped_cnts

def destroy_blocks(line, d, s):
  '''d방향으로 거리가 s이하인 모든 칸 삭제'''
  idx = 0
  d_idx = 0
  if d == 3:
    idx = 0
    d_idx = 9 
  elif d == 2:
    idx = 2
    d_idx = 11
  elif d == 4:
    idx = 4
    d_idx = 13
  elif d == 1:
    idx = 6
    d_idx = 15
  
  for _ in range(s):
    if idx < len(line):
      line[idx] = 0
    idx += d_idx
    d_idx+=8

def get_new_line(N, line):
  '''새로운 블럭 생성'''
  new_line = []

  groups = get_groups(line)
  for group in groups:
    new_line.append(len(group))
    new_line.append(line[group[-1]])

    if len(new_line) >= N*N-1:
      break

  return new_line[:N*N-1]

N, M = input_n(int)
table = [input_n(int) for _ in range(N)]
line = get_line(N, table)
cnts = [0,0,0]

for _ in range(M):
  d, s = input_n(int)
  destroy_blocks(line, d, s)
  while True:
    poped_cnts = pop_blocks(line)
    if sum(poped_cnts) == 0:
      break

    for i in range(3):
      cnts[i] += poped_cnts[i]

    move_center(line)
  line = get_new_line(N, line)

print(cnts[0] + cnts[1] * 2 + cnts[2] * 3)