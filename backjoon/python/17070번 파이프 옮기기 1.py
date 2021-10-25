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

N = int(input())
table = [input_n(int) for _ in range(N)]

PIPE = [
  [(0,0)],
  [(0,0)],
  [(-1,0), (0,-1), (0,0)]
]

cnt = [[[0,0,0] for _ in range(N)] for _ in range(N)]
cnt[0][1][0] = 1
def ok(i,j,p_type):
  if 0<=i<N and 0<=j<N:
    for pi,pj in PIPE[p_type]:
      if table[i+pi][j+pj] != 0:
        return False
    return True
  else: return False

for k in range(1, N):
  P = [(k, j) for j in range(0,k)] + [(i, k) for i in range(0,k)] + [(k,k)]
  for i,j in P:
    # left
    if ok(i,j+1,0):
      cnt[i][j+1][0] += cnt[i][j][0] + cnt[i][j][2]
    # down
    if ok(i+1,j,1):
      cnt[i+1][j][1] += cnt[i][j][1] + cnt[i][j][2]
    # left-down
    if ok(i+1,j+1,2):
      cnt[i+1][j+1][2] += cnt[i][j][0] + cnt[i][j][1] + cnt[i][j][2]

print(sum(cnt[-1][-1]))