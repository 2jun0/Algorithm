import sys
def input(_type=str):
	return _type(sys.stdin.readline().strip())

INF = 10**10
max_cnt = 0
def dfs(x, cost, cnt, bitmask):
  global max_cnt

  if costs[x][bitmask] <= cost:
    return

  max_cnt = max(max_cnt, cnt)
  costs[x][bitmask] = cost

  for other in range(N):
    if graph[x][other] >= cost and not bitmask&(1<<other):
      dfs(other, graph[x][other], cnt+1, bitmask|(1<<other))

N = input(int)
graph = [list(map(int, input(str))) for _ in range(N)]
costs = [[INF]*(1<<N) for _ in range(N)]

dfs(0, 0, 1, 1<<0)

print(max_cnt)