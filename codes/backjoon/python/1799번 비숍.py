import sys
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

N = input(int)
table = [input_n(int) for _ in range(N)]
even_L, odd_L = [], []
for y in range(N):
  for x in range(N):
    table[y][x] = 0 if table[y][x] == 1 else 1

    if table[y][x] == 0:
      if (x+y)%2 == 0: even_L.append((y,x))
      else: odd_L.append((y,x))

def put_bishop(y, x, v = 1):
  # 정방향
  ty, tx = y, x
  while 0 < ty and 0 < tx: ty, tx = ty - 1, tx - 1 # 좌상단 찾기
  while ty < N and tx < N:
    table[ty][tx] += v
    ty, tx = ty + 1, tx + 1
  # 사선방향
  ty, tx = y, x
  while 0 < ty and tx < N-1: ty, tx = ty - 1, tx + 1 # 우상단 찾기
  while ty < N and 0 <= tx:
    table[ty][tx] += v
    ty, tx = ty + 1, tx - 1

def dfs(L, idx):
  max_cnt = 0

  y,x = L[idx]
  put_bishop(y,x)
  for ni in range(idx+1, len(L)):
    ny,nx = L[ni]
    if table[ny][nx] == 0:
      max_cnt = max(max_cnt, dfs(L, ni))
  put_bishop(y,x,-1)

  return max_cnt+1

max_even_cnt = 0
for i in range(len(even_L)):
  max_even_cnt = max(max_even_cnt, dfs(even_L, i))
max_odd_cnt = 0
for i in range(len(odd_L)):
  max_odd_cnt = max(max_odd_cnt, dfs(odd_L, i))

print(max_even_cnt + max_odd_cnt)