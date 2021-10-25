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

N, M = input_n(int)
table = []
for _ in range(N):
  table.append([])
  L = input()
  for x in L: table[-1].append(int(x))

max_l = -1
for l in range(N, 0, -1):
  for i in range(N-l+1):
    i1, i2 = i, i+l-1
    for j in range(M-l+1):
      j1, j2 = j, j+l-1
      flag = True
      for ti, tj in [(i1,j2),(i2,j1),(i2,j2)]:
        flag &= table[i1][j1] == table[ti][tj]
      if flag: max_l = l
    if max_l != -1: break
  if max_l != -1: break

print(max_l**2)
      