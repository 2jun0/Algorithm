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

N, M = input_n(int)
table = [input_n(int) for _ in range(N)]

def bfs():
  T = [[t for t in L] for L in table]
  def ok(i,j):
    return 0<=i<N and 0<=j<M and T[i][j] == 0

  s1, s2 = [], []
  for i in range(N):
    for j in range(M):
      if T[i][j] == 2:
        s2.append((i,j))

  while len(s2) > 0:
    s1, s2 = s2, s1
    while len(s1) > 0:
      i,j = s1.pop()
      T[i][j] = 2
      
      for ti, tj in [(i-1,j), (i+1,j), (i,j-1), (i,j+1)]:
        if ok(ti,tj): s2.append((ti,tj))
  cnt = 0
  for L in T:
    for t in L:
      if t == 0: cnt+=1

  return cnt

result = 0
T2 = [(i,j) for j in range(M) for i in range(N)]
def make_wall(cnt):
  global result
  if cnt == 3:
    result = max(result, bfs())
    return
  for i,j in T2:
    if table[i][j] == 0:
      table[i][j] = 1
      make_wall(cnt+1)
      table[i][j] = 0

make_wall(0)
print(result)
