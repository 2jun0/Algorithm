import sys
sys.setrecursionlimit(10000000) # 재귀 제한 풀기
INF = 10**8
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))
def print_n(L, join_str=' '):
  for i,l in enumerate(L): print(l, end=join_str if i<len(L)-1 else '\n')
def LL(n,m,d=0): return [[d]*n for _ in range(m)]

R, C, T = input_n(int)
table = [input_n(int) for _ in range(R)]
machine = []
for i in range(R):
  if table[i][0] == -1:
    machine.append((i,0))
    machine.append((i+1,0))
    break

def diffuse():
  global table
  def ok(i,j):
    return 0<=i<R and 0<=j<C and table[i][j] != -1
  new_table = [[0]*C for _ in range(R)]
  for i,j in machine: new_table[i][j] = -1
  for i in range(R):
    for j in range(C):
      if table[i][j] > 0:
        cnt = 0
        for ti, tj in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
          if ok(ti,tj):
            new_table[ti][tj] += table[i][j]//5
            cnt+=1
        new_table[i][j] += int(table[i][j]-table[i][j]//5*cnt)
  table = new_table 

def clean():
  mx1 = machine[0][0]
  mx2 = machine[1][0]
  T = []
  for y in range(1, C-1): T.append((mx1,y))
  for x in range(mx1, 0, -1): T.append((x,C-1))
  for y in range(C-1,0,-1): T.append((0,y))
  for x in range(0, mx1): T.append((x,0))
  tmp = 0
  for i, j in T: table[i][j], tmp = tmp, table[i][j]
  T = []
  for y in range(1, C-1): T.append((mx2,y))
  for x in range(mx2, R-1): T.append((x,C-1))
  for y in range(C-1,0,-1): T.append((R-1,y))
  for x in range(R-1, mx2, -1): T.append((x,0))
  tmp = 0
  for i, j in T: table[i][j], tmp = tmp, table[i][j]
  

for _ in range(T):
  diffuse()
  clean()
result = 0
for L in table: result += sum(L)
print(result+2)