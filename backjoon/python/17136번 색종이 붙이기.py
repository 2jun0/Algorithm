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
def getLRUD(i,j): return [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]

table = [input_n(int) for _ in range(10)]
A = []
for y in range(10):
  for x in range(10):
    if table[y][x] == 1:
      A.append((y,x))
cnts = [0]*6

def func(ai):
  y,x = A[ai]
  min_cnt = INF
  for r in range(1,6):
    if not(y+r-1<10 and x+r-1<10 and cnts[r] < 5): continue

    flag = True
    for ry in range(y, y+r):
      for rx in range(x, x+r):
        if table[ry][rx] != 1:
          flag = False
          break
      if not flag: break
    
    if not flag: continue

    cnts[r] += 1
    for ry in range(y, y+r):
      for rx in range(x, x+r):
        table[ry][rx] = 0
    
    next_ai = None
    for tai in range(ai+1, len(A)):
      ty, tx = A[tai]
      if table[ty][tx] == 1:
        next_ai = tai
        break

    if next_ai == None:
      for ry in range(y, y+r):
        for rx in range(x, x+r):
          table[ry][rx] = 1
      cnts[r] -= 1
      return 1
    else:
      min_cnt = min(min_cnt, func(next_ai) + 1)
  
      for ry in range(y, y+r):
        for rx in range(x, x+r):
          table[ry][rx] = 1
      cnts[r] -= 1
  return min_cnt

if len(A) == 0:
  print(0)
else:
  cnt = func(0)
  if cnt >= INF:
    print(-1)
  else:
    print(cnt)
