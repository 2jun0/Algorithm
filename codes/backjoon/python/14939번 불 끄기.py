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

table = [input() for _ in range(10)]

def turn_on(mask,i,j):
  for ti, tj in [(i,j),(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
    if 0<=ti<10 and 0<=tj<10:
      if mask & 1<<(ti*10+tj) != 0: mask ^= 1<<(ti*10+tj)
      else: mask |= 1<<(ti*10+tj)
  return mask

def func(mask):
  cnt = 0
  for i in range(9):
    for j in range(10):
      if mask & 1<<(i*10+j) != 0:
        cnt += 1
        mask = turn_on(mask,i+1,j)
  if mask != 0: return INF
  else: return cnt

def table2mask():
  mask = 0
  for i in range(10):
    for j in range(10):
      if table[i][j] == 'O':
        mask |= 1<<(j+i*10)
  return mask

def dfs(j, mask):
  if j == 10:
    return func(mask)
  else:
    cnt = min(
      dfs(j+1,mask),
      dfs(j+1,turn_on(mask,0,j))+1
    )
    return cnt

cnt = dfs(0,table2mask())
if cnt >= INF: print(-1)
else: print(cnt)