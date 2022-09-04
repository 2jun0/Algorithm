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

N, M = input_n(int)
table = [input() for _ in range(N)]

visited = [[False]*M for _ in range(N)]

def dfs(i,j):
  if visited[i][j]: return 0
  visited[i][j] = True

  sum_cnt = 1
  for ti, tj in getLRUD(i,j):
    if 0<=ti<N and 0<=tj<M and table[ti][tj] == '0':
      sum_cnt += dfs(ti,tj)
  return sum_cnt%10

A = [[0]*M for _ in range(N)]
A_sig = [[0]*M for _ in range(N)]
visited2 = [[False]*M for _ in range(N)]

def dfs2(i,j,v,sig):
  if visited2[i][j]: return
  visited2[i][j] = True
  A[i][j] = v
  A_sig[i][j] = sig

  for ti, tj in getLRUD(i,j):
    if 0<=ti<N and 0<=tj<M and table[ti][tj] == '0':
      dfs2(ti,tj,v,sig)

sig = 1
for i in range(N):
  for j in range(M):
    if not visited[i][j] and table[i][j] == '0':
      cnt = dfs(i,j)
      dfs2(i,j,cnt,sig)
      sig+=1


B = [[0]*M for _ in range(N)]

for i in range(N):
  for j in range(M):
    if table[i][j] == '1':
      B[i][j] = 1
      sigs = []
      for ti, tj in getLRUD(i,j):
        if 0<=ti<N and 0<=tj<M and table[ti][tj] == '0' and A_sig[ti][tj] not in sigs:
          B[i][j] += A[ti][tj]
          sigs.append(A_sig[ti][tj])
      B[i][j] %= 10

for L in B:
  print_n(L,'')