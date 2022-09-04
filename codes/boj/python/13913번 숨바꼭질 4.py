from collections import deque
import sys
INF = 10**10
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

N, K = input_n(int)

def bfs():
  costs = [INF] * 100001
  parents = [INF] * 100001

  costs[N] = 0;
  q = deque([N])

  while q:
    x = q.popleft()

    # 수빈이 동생을 찾음
    if x == K:
      break
    
    # bfs로 수빈이 이동. 
    for t_x in [x-1, x+1, x*2]:
      if 0<=t_x<=100000 and costs[t_x] > costs[x]:
        costs[t_x] = costs[x] + 1
        parents[t_x] = x
        q.append(t_x)
  
  # 부모 노드를 찾아서 results에 기록함.
  x = K
  results = ''
  while x != N:
    results = str(x)+' '+results
    x = parents[x]
  results = str(x)+' '+results # x == N

  return costs[K], results.rstrip()

cost, results = bfs()
print(cost, results, sep='\n')