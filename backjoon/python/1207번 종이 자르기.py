import sys
INF = 10**10
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))
def print_n(L, join_str=' '):
  for i,l in enumerate(L): print(l, end=join_str if i<len(L)-1 else '\n')
def LL(n,m,d=0): return [[d]*n for _ in range(m)]
def avg(l): return sum(l)/len(l)
def getLRUD(i,j): return [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]

L = input(int)
A = []
for i in range(5):
  A.append([])
  N, M = input_n(int)
  table = [input() for _ in range(N)]

  for y, Line in enumerate(table):
    for x, a in enumerate(Line):
      if a == '#':
        A[i].append((y,x))
  
  # starting point
  sy, sx = A[i][0]
  # set to relative point
  for a_i, apos in enumerate(A[i]):
    ay, ax = apos
    A[i][a_i] = [ay-sy, ax-sx]

def bind(table, sy, sx, i):
  for y, x in A[i]:
    if 0<=sy+y<L and 0<=sx+x<L and table[sy+y][sx+x] == 0:
      table[sy+y][sx+x] = i+1
    else:
      return False
  return True

def unbind(table, sy, sx, i):
  for y, x in A[i]:
    if 0<=sy+y<L and 0<=sx+x<L and table[sy+y][sx+x] == i+1:
      table[sy+y][sx+x] = 0
    else:
      break

def dfs(table, visited):
  # Get start point
  sy, sx = -1, -1
  for y in range(L):
    for x in range(L):
      if table[y][x] == 0:
        sy, sx = y, x
        break
    if sy != -1: break

  # Finish
  if sy == -1 and sx == -1:
    flag = True
    for v in visited: flag &= v
    return flag

  # Dfs next level
  for i in range(5):
    if visited[i]: continue

    if bind(table, sy, sx, i):
      visited[i] = True
      if dfs(table, visited):
        return True
      visited[i] = False
    unbind(table, sy, sx, i)
  
  return False
table = LL(L, L)
if dfs(table, [False]*5):
  for Line in table:
    print_n(Line, '')
else:
  print('gg')

