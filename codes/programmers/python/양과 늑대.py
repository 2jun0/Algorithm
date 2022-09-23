from collections import deque

def get_max_sheep_cnt_bfs(info, graph):
  visited = [False]*(1<<len(info))
  q = deque()

  visited[1<<0] = True
  # visited, nexts
  q.append((1<<0, graph[0], 1, 0))

  max_sheep_cnt = 0

  while q:
    bitmask, nexts, sheep_cnt, wolf_cnt = q.popleft()

    if sheep_cnt <= wolf_cnt:
      continue

    max_sheep_cnt = max(max_sheep_cnt, sheep_cnt)

    for next in nexts:
      new_bitmask = bitmask | 1<<next
      if visited[new_bitmask]:
        continue

      visited[new_bitmask] = True

      new_nexts = []
      for new_next in graph[next]:
        new_nexts.append(new_next)
      for new_next in nexts:
        if next != new_next:
          new_nexts.append(new_next)

      if info[next] == 0:
        q.append((bitmask | 1<<next, new_nexts, sheep_cnt+1, wolf_cnt))
      else:
        q.append((bitmask | 1<<next, new_nexts, sheep_cnt, wolf_cnt+1))

  return max_sheep_cnt

def solution(info, edges):
  graph = [[] for _ in range(len(info))]
  for srt, dest in edges:
    graph[srt].append(dest)

  max_sheep_cnt = get_max_sheep_cnt_bfs(info, graph)
  return max_sheep_cnt