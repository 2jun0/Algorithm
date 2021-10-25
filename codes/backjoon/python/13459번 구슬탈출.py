import sys
sys.setrecursionlimit(10000000) # 재귀 제한 풀기
INF = 10**10
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))
def print_n(L, join_str=' '):
  for i,l in enumerate(L): print(l, end=join_str if i<len(L)-1 else '\n')
def LL(n,m,d=0): return [[d]*n for _ in range(m)]
def avg(l): return sum(l)/len(l)

N, M = input_n(int)

table = [input() for _ in range(N)]

for y, l in enumerate(table):
  for x, a in enumerate(l):
    if a == 'R': 
      red = (y,x)
      table[y] = table[y][:x]+'.'+table[y][x+1:]
    elif a == 'B': 
      blue = (y,x)
      table[y] = table[y][:x]+'.'+table[y][x+1:]

LEFT, RIGHT, UP, DOWN = (0,-1), (0,1), (-1,0), (1,0)
def move_one(d, a, b):
  y,x = a
  if y == -1 or x == -1: return (y,x)

  while table[y+d[0]][x+d[1]] != '#' and (y+d[0]!=b[0] or x+d[1]!=b[1]):
    y,x = y+d[0],x+d[1]
    if table[y][x] == 'O': return (-1, -1)
  return (y,x)
def move_all(d, red, blue):
  red = move_one(d,red,blue)
  blue = move_one(d,blue,red)
  red = move_one(d,red,blue)
  return red, blue

s1 = []
s2 = [(red, blue)]
cnt = 0
flag = False
while len(s2) > 0:
  visited=[[LL(M,N,False) for _ in range(M)] for _ in range(N)]
  s1,s2 = s2,s1
  while len(s1) > 0:
    red, blue = s1.pop()
    if red == (-1,-1) and blue != (-1,-1): 
      flag = True
      break
    if red == (-1,-1) and blue == (-1,-1): continue
    if visited[red[0]][red[1]][blue[0]][blue[1]]: continue
    if cnt >= 10: continue

    visited[red[0]][red[1]][blue[0]][blue[1]] = True

    s2.append(move_all(LEFT, red, blue))
    s2.append(move_all(RIGHT, red, blue))
    s2.append(move_all(UP, red, blue))
    s2.append(move_all(DOWN, red, blue))
  if flag: break
  cnt+=1
if flag:
  print(1)
else:
  print(0)