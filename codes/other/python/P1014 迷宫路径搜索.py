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

table = [
  '.#...',
  '.#.#.',
  '.....',
  '.#.#.']

y,x = input_n(int)
y,x=y-1,x-1

result = []
def func(y,x,L):
  if not(0<=y<4 and 0<=x<5): return
  if table[y][x] == '#': return
  for ty,tx in L:
    if ty == y and tx == x: return

  L = L+[(y,x)]
  if y == 3 and x == 4:
    LL = []
    for ty,tx in L:
      LL.append('({},{})'.format(ty+1,tx+1))
    result.append(LL)
  else:
    for ty, tx in [(y-1,x),(y+1,x),(y,x-1),(y,x+1)]:
      func(ty, tx, L)
func(y,x,[])

if len(result)>0:
  print('Path:')
  for LL in result:
    print_n(LL)
else:
  print('No Entrance')