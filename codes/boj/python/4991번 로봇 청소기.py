from collections import deque
import sys
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

INF = 10**10
while True:
  def get_dist(src_idx):
    dists = [[[INF]*w for _ in range(h)] for _ in range(1<<len(points))]
    q = deque()

    sy, sx = points[src_idx]
    dists[1<<src_idx][sy][sx] = 0
    q.append((1<<src_idx, sy, sx))

    while q:
      bitmask, y, x = q.popleft()

      if bitmask == (1<<len(points))-1:
        return dists[bitmask][y][x]

      for ny, nx in [(y+1,x),(y-1,x),(y,x+1),(y,x-1)]:
        if 0<=ny<h and 0<=nx<w and table[ny][nx] != 'x':
          # get next bit mask
          nxt_bitmask = bitmask
          nxt_idx = point2idx.get((ny,nx), -1)
          if nxt_idx >= 0:
            nxt_bitmask |= 1<<nxt_idx

          if dists[nxt_bitmask][ny][nx] != INF:
            continue

          dists[nxt_bitmask][ny][nx] = dists[bitmask][y][x] + 1
          q.append((nxt_bitmask,ny,nx))
    
    return -1

  w, h = input_n(int)
  if w == 0 and h == 0:
    break

  table = [input(str) for _ in range(h)]

  start = None
  points = []

  for y in range(h):
    for x in range(w):
      if table[y][x] == 'o':
        start = (y,x)
      if table[y][x] == '*':
        points.append((y,x))

  points = [start] + points
  point2idx = {
    point: idx for idx, point in enumerate(points)
  }

  print(get_dist(0))