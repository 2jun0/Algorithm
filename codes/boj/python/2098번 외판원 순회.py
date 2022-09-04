from collections import deque
import sys
INF = 10**8
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

N = input(int)
W = [input_n(int) for _ in range(N)]
for i in range(N):
  for j in range(N):
    if i!=j and W[i][j] == 0:
      W[i][j] = INF
      
def bfs():
  dists = [[INF]*(1<<N) for _ in range(N)]
  # x, visited_bits
  # x: 마지막 위치
  # visited_bits: 지나왔던 위치들
  q = deque([])
  q.append((0,1<<0))
  dists[0][1<<0] = 0
  
  min_result = INF

  while q:
    x, vistied_bits = q.popleft()

    if vistied_bits == (1<<N)-1:
      min_result = min(min_result, dists[x][vistied_bits] + W[x][0])
      continue

    for y in range(N):
      if (1<<y) & vistied_bits or W[x][y] == INF: continue

      # 이미 한번 간 경우 탐색노드를 중첩하지 않음 
      # (BFS라서 이런 조건이 걸렸을때, 중복노드는 큐에 남아있는다.)
      if dists[y][vistied_bits|(1<<y)] == INF:
        q.append((y,vistied_bits|(1<<y)))
      
      dists[y][vistied_bits|(1<<y)] = min(dists[y][vistied_bits|(1<<y)], dists[x][vistied_bits]+W[x][y])
  
  return min_result

print(bfs())