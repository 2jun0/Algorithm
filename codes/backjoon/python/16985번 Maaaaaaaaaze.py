from collections import deque
from itertools import permutations, product
import sys

INF = 10**10
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
  return list(map(_type, input().split()))

def bfs(cube, start_y, start_x, end_y, end_x):
  dists = [[[INF]*5 for _ in range(5)] for _ in range(5)]
  q = deque()

  dists[0][start_y][start_x] = 0
  q.append((0, start_y, start_x))

  while q:
    z, y, x = q.popleft()

    if z == 4 and y == end_y and x == end_x:
      break

    for n_z, n_y, n_x in [(z-1,y,x),(z+1,y,x),(z,y-1,x),(z,y+1,x),(z,y,x-1),(z,y,x+1)]:
      if 0<=n_z<5 and 0<=n_y<5 and 0<=n_x<5 and \
        cube[n_z][n_y][n_x] == 1 and dists[n_z][n_y][n_x] == INF:

        dists[n_z][n_y][n_x] = dists[z][y][x] + 1
        q.append((n_z,n_y,n_x))

  return dists[4][end_y][end_x]


def turn_plate(plate, angle):
  n_plate = [[0]*5 for _ in range(5)]

  if angle == 0:
    for y in range(5):
      for x in range(5):
        n_plate[y][x] = plate[y][x]

  elif angle == 1:
    for y in range(5):
      for x in range(5):
        n_plate[x][4-y] = plate[y][x]

  elif angle == 2:
    for y in range(5):
      for x in range(5):
        n_plate[4-y][4-x] = plate[y][x]

  elif angle == 3:
    for y in range(5):
      for x in range(5):
        n_plate[4-x][y] = plate[y][x]
  
  return n_plate

def stack_plates(turned_plates, idxes, angles):
  cube = []

  for idx, angle in zip(idxes, angles):
    cube.append(turned_plates[idx][angle])
  
  return cube
          

plates = [[input_n(int) for _ in range(5)] for _ in range(5)]
all_angles_cases = list(product(*[[0,1,2,3]]*5))
all_stack_idxes_cases = list(permutations([0,1,2,3,4], 5))

turned_plates = [[[[0]*5 for _ in range(5)] for _ in range(4)] for _ in range(5)]
for plate_idx in range(5):
  for angle in range(4):
    turned_plates[plate_idx][angle] = turn_plate(plates[plate_idx], angle)

min_dist = INF
for angles_case in all_angles_cases:
  for stack_idxes_case in all_stack_idxes_cases:
    cube = stack_plates(turned_plates, stack_idxes_case, angles_case)

    if cube[0][0][0] == 1 and cube[4][4][4] == 1:
      min_dist = min(min_dist, bfs(cube, 0, 0, 4, 4))

print(-1 if min_dist == INF else min_dist)