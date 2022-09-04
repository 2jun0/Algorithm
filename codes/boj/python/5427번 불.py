from collections import deque
import sys
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
  return list(map(_type, input().split()))

# 4179번 불! 참고

def bfs(table, J, Fs):
  C, R = len(table[0]), len(table)
  dists_J = [[-1]*C for _ in range(R)]
  dists_F = [[-1]*C for _ in range(R)]

  q = deque()
  for y, x in Fs:
    dists_F[y][x] = 0
    q.append((y,x,'F'))
  dists_J[J[0]][J[1]] = 0
  q.append((J[0],J[1],'J'))

  while q:
    y, x, flag = q.popleft()

    if flag == 'J' and (y in [0,R-1] or x in [0,C-1]):
      return dists_J[y][x] + 1

    for n_y, n_x in [(y+1, x),(y-1, x),(y, x+1),(y, x-1)]:
      if 0<=n_y<R and 0<=n_x<C and table[n_y][n_x] != '#':
        if flag == 'F' and dists_F[n_y][n_x] == -1:
          dists_F[n_y][n_x] = dists_F[y][x] + 1
          q.append((n_y, n_x, flag))
        if flag == 'J' and dists_J[n_y][n_x] == -1 and dists_F[n_y][n_x] == -1:
          dists_J[n_y][n_x] = dists_J[y][x] + 1
          q.append((n_y, n_x, flag))
    
  return 'IMPOSSIBLE'


T = input(int)
for _ in range(T):
  C, R = input_n(int)
  table = [input() for _ in range(R)]

  # find J and Fs
  J = None
  Fs = []
  for y in range(R):
    for x in range(C):
      if table[y][x] == '@':
        J = (y,x)
      elif table[y][x] == '*':
        Fs.append((y,x))

  print(bfs(table, J, Fs))