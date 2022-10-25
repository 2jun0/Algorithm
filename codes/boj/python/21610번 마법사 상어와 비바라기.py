import sys
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

def move_clouds(N, clouds, d, s):
  '''구름 움직임'''
  for idx, cloud in enumerate(clouds):
    clouds[idx] = ((cloud[0] + dy[d]*s) % N, (cloud[1] + dx[d]*s) % N)

def rain(A, clouds):
  '''각 구름에서 비가 내림'''
  for cy, cx in clouds:
    A[cy][cx] += 1

def magic_copy_water(N, A, poses):
  '''물복사버그 마법 시전!'''
  for y, x in poses:
    crs_having_water_cnt = 0

    for ny, nx in [(y-1,x-1), (y-1,x+1), (y+1,x-1), (y+1,x+1)]:
      if 0<=ny<N and 0<=nx<N and A[ny][nx] >= 1:
        crs_having_water_cnt += 1

    A[y][x] += crs_having_water_cnt

def create_clouds(N, A, excepts):
  '''물의 양이 2 이상인 칸에 새로 구름을 생성해서 반환'''
  clouds = []

  for y in range(N):
    for x in range(N):
      if A[y][x] >= 2 and (y,x) not in excepts:
        clouds.append((y,x))
        A[y][x] -= 2

  return clouds
  
dy = [0, -1, -1, -1, 0, 1, 1, 1]
dx = [-1, -1, 0, 1, 1, 1, 0, -1]

N, M = input_n(int)
A = [input_n(int) for _ in range(N)]
clouds = [(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)]

for _ in range(M):
  _d, s = input_n(int)
  d = _d-1
  move_clouds(N, clouds, d, s)
  rain(A, clouds)
  magic_copy_water(N, A, clouds)
  clouds = create_clouds(N, A, clouds)

print(sum(sum(line) for line in A))