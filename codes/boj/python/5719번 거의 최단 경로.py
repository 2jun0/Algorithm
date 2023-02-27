from collections import defaultdict, deque
import heapq
import sys
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

INF = 10**8

def get_reversed_routes(N, routes, src):
  '''routes를 거꾸로 뒤집음'''
  reversed_routes = defaultdict(set)
  q = deque()
  visited = [False]*N

  q.append(src)
  visited[src] = True
  while q:
    x = q.popleft()

    for prev in routes[x]:
      reversed_routes[prev].add(x)
      if not visited[prev]:
        visited[prev] = True
        q.append(prev)
  
  return reversed_routes

def get_min_dist_and_routes_dijkstra(N, graph, src, dst):
  '''다이스트라 알고리즘으로 최소거리, 최소경로를 찾음'''
  dists = [INF] * N
  min_dist_reverse_routes = defaultdict(set)

  dists[src] = 0
  h = [(dists[src], src)]

  while h:
    d, x = heapq.heappop(h)

    if d > dists[x]:
      continue

    for nxt, x2nxt_d in graph[x]:
      nxt_dist = dists[x] + x2nxt_d
      if dists[nxt] > nxt_dist:
        dists[nxt] = nxt_dist
        min_dist_reverse_routes[nxt].clear()
        min_dist_reverse_routes[nxt].add(x)
        heapq.heappush(h, (nxt_dist, nxt))
      elif dists[nxt] == nxt_dist:
        min_dist_reverse_routes[nxt].add(x)

  return dists[dst], get_reversed_routes(N, min_dist_reverse_routes, dst)

def remove_routes_in_graph(N, graph, routes):
  '''그래프에서 경로를 제외함'''
  for x in range(N):
    new_lines = []

    for nxt, d in graph[x]:
      if nxt not in routes[x]:
        new_lines.append((nxt, d))

    graph[x] = new_lines

while True:
  N, M = input_n(int)
  if N == 0 and M == 0:
    break

  S, D = input_n(int)
  graph = defaultdict(list)
  for _ in range(M):
    U, V, P = input_n(int)
    graph[U].append((V, P))

  _, min_dist_routes = get_min_dist_and_routes_dijkstra(N, graph, S, D)
  remove_routes_in_graph(N, graph, min_dist_routes)

  almost_min_dist, _ = get_min_dist_and_routes_dijkstra(N, graph, S, D)
  print(almost_min_dist if almost_min_dist != INF else -1)