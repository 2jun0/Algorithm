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

T = input(int)
for _ in range(T):
  N = input(int)
  A = [input_n(int) for _ in range(N)]

  visited = [False] * N

  min_v = [INF, INF]

  def update_min_v():
    global min_v
    val = [0,0]
    for i in range(N):
      if visited[i]:
        val[0] += A[i][0]
        val[1] += A[i][1]
      else:
        val[0] -= A[i][0]
        val[1] -= A[i][1]
    
    if min_v[0]**2 + min_v[1]**2 > val[0]**2 + val[1]**2:
      min_v[0], min_v[1] = val[0], val[1]
    return min_v

  def dfs(x, lv):
    
    if visited[x]: return
    visited[x] = True

    if lv >= N//2: 
      update_min_v()
    else: 
      for y in range(x+1,N): dfs(y, lv+1)
    visited[x] = False

  for i in range(N//2+1): dfs(i,1)
  
  print((min_v[0]**2 + min_v[1]**2) ** 0.5)