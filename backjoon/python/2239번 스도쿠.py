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

table = [input() for _ in range(9)]
for i in range(9): table[i] = [int(table[i][j]) for j in range(9)]
zeros = []
i_ok_table = [[True]*10 for _ in range(9)]
j_ok_table = [[True]*10 for _ in range(9)]
a_ok_table = [[[True]*10 for _ in range(3)] for __ in range(3)]

for i in range(9):
  ai = i//3
  for j in range(9):
    i_ok_table[i][table[i][j]] = False
    j_ok_table[j][table[i][j]] = False
    aj = j//3
    a_ok_table[ai][aj][table[i][j]] = False
    
    if table[i][j] == 0: zeros.append((i,j))
def func(z_i):
  if z_i >= len(zeros): return True
  i,j = zeros[z_i]
  ai, aj = i//3, j//3
  for x in range(1, 10):
    if not(i_ok_table[i][x] & j_ok_table[j][x] & a_ok_table[ai][aj][x]): continue
    table[i][j] = x
    i_ok_table[i][x] = False
    j_ok_table[j][x] = False
    a_ok_table[ai][aj][x] = False
    if func(z_i+1):
      return True
    table[i][j] = 0
    i_ok_table[i][x] = True
    j_ok_table[j][x] = True
    a_ok_table[ai][aj][x] = True
  return False

func(0)
for L in table: print_n(L, '')