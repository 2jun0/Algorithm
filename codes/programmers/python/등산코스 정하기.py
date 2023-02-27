import heapq

def solution(n, paths, gates, summits):
  graph = [{} for _  in range(n+1)]

  for a, b, dist in paths:
    graph[a][b] = dist
    graph[b][a] = dist

  is_summit = [False]*(n+1)
  for x in summits:
    is_summit[x] = True

  def bfs():
    visited = [False]*(n+1)
    candidates = []
    hq = []

    for gate in gates:
      heapq.heappush(hq, (0, gate))
    
    min_intensity = 10**10
    while hq:
      intensity, x = heapq.heappop(hq)

      if visited[x]:
        continue

      visited[x] = True

      if min_intensity < intensity:
        break

      if is_summit[x]:
        min_intensity = intensity
        candidates.append(x)
        continue

      for n_x, dist in graph[x].items():
        heapq.heappush(hq, (max(intensity, dist), n_x))

    candidates.sort()
    return [candidates[0], min_intensity]

  return bfs()

