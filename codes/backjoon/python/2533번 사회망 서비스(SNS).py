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
def getLRUD(i,j): return [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]

N = input(int)
graph = LL(0,N+1)

# 얼리어답터, 얼리어답터친구
dp = LL(2,N+1,INF)

for _ in range(N-1):
  u, v = input_n(int)
  graph[u].append(v)
  graph[v].append(u)

visited = [False]*(N+1)

def treeize(x):
  visited[x] = True

  new_graph_x = []
  for y in graph[x]:
    if not visited[y]:
      new_graph_x.append(y)

  graph[x] = new_graph_x

def cal_dp(x):
  # type 0: 얼리어답터
  dp[x][0] = 1
  for y in graph[x]:
    dp[x][0] += min(dp[y])

  # type 1: 얼리어답터친구
  dp[x][1] = 0
  for y in graph[x]:
    dp[x][1] += dp[y][0]

# tree 변환
s = [1]
s2 = []
while len(s) > 0:
  x = s.pop()
  s2.append(x)
  treeize(x)
  for y in graph[x]:
    if not visited[y]:s.append(y)
# dp구하기
while len(s2) > 0:
  x = s2.pop()
  cal_dp(x)

print(min(dp[1]))