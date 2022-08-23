INF = 10**10
def solution(sizes):
  max_w, max_h = 0, 0
  for w, h in sizes:
    w, h = min(w,h), max(w,h)

    max_w = max_w
  dfs(0, 0, 0)
  return min_size