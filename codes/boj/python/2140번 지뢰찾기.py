import sys

def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

MINE = 'O'
NOT_MINE = 'X'

def find_mine(table, y, x):
  cnt = int(table[y][x])
  for ny, nx in [(y-1,x-1), (y-1,x), (y-1,x+1), (y,x-1), (y,x+1), (y+1,x-1), (y+1,x), (y+1,x+1)]:
    if 0<=ny<N and 0<=nx<N:
      if table[ny][nx] == '#':
        if cnt > 0:
          table[ny][nx] = MINE
        else:
          table[ny][nx] = NOT_MINE
      
      if table[ny][nx] == MINE:
        cnt -= 1
    

N = input(int)
table = [list(map(str, input())) for _ in range(N)]

for y in range(N):
  for x in range(N):
    if table[y][x] not in ['#', MINE, NOT_MINE]:
      find_mine(table, y, x)
cnt = 0   
for y in range(N):
  for x in range(N):
    if table[y][x] in [MINE, '#']:
      cnt += 1

print(cnt)