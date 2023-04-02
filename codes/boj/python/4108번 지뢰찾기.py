import sys

def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))  

while True:
  cmds = input_n(int)
  if len(cmds) != 2:
    break

  R, C = cmds
  table = [list(input()) for _ in range(R)]

  dy = [-1, -1, -1, 0, 0, 1, 1, 1]
  dx = [-1, 0, 1, -1, 1, -1, 0, 1]

  for y in range(R):
    for x in range(C):
      if table[y][x] == '*':
        continue
      
      table[y][x] = 0
      for ay, ax in zip(dy, dx):
        ny = y + ay
        nx = x + ax
        if 0<=ny<R and 0<=nx<C:
          if table[ny][nx] == '*':
            table[y][x] += 1
      table[y][x] = str(table[y][x])

  for line in table:
    print(''.join(line))