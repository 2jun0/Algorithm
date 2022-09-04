import sys
sys.setrecursionlimit(15000)
def input(_type = str):
  return _type(sys.stdin.readline().strip())
def input_n(_type = str):
  return list(map(_type, input(str).split()))

def can_go(start, end, weight):
  visited = [False]*N

  def dfs(x):
    if x == end:
      return True

    visited[x] = True

    flag = False
    for n_x, max_weight in graph[x].items():
      if not visited[n_x] and max_weight >= weight:
        flag |= dfs(n_x)
        
    return flag

  return dfs(start)

def find_max_weight(start, end):
  # 클 수록 False가 됨
  left, right = 1, 1000000000

  while left < right:
    mid = (left + right) // 2
    if not can_go(start, end, mid):
      right = mid
    else:
      left = mid+1
  
  if can_go(start, end, right):
    return right
  else:
    return right-1

N, M = input_n(int)
graph = [{} for _ in range(N)]

for _ in range(M):
  A, B, C = input_n(int)
  A, B = A-1, B-1

  if B in graph[A]:
    graph[A][B] = max(graph[A][B], C)
    graph[B][A] = max(graph[B][A], C)
  else:
    graph[A][B] = C
    graph[B][A] = C

start, end = input_n(int)
start, end = start - 1, end - 1
print(find_max_weight(start, end))