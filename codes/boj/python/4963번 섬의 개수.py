import sys
sys.setrecursionlimit(10000)

def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

def travel_island(table, visited, h, w, y, x):
  visited[y][x] = True

  for ny, nx in [(y-1,x-1), (y-1,x), (y-1,x+1), (y,x-1), (y,x+1), (y+1,x-1), (y+1,x), (y+1,x+1)]:
    if 0<=ny<h and 0<=nx<w and table[ny][nx] == 1 and not visited[ny][nx]:
      travel_island(table, visited, h, w, ny, nx)

def get_island_cnt(table, h, w):
  visited = [[False] * w for _ in range(h)]
  cnt = 0

  for y in range(h):
    for x in range(w):
      if table[y][x] == 1 and not visited[y][x]:
        cnt += 1
        travel_island(table, visited, h, w, y, x)

  return cnt

while True:
  w, h = input_n(int)
  if w==0 and h==0:
    break

  table = [input_n(int) for _ in range(h)]

  print(get_island_cnt(table, h, w))