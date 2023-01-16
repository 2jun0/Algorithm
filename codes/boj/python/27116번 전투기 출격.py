import sys
def input(_type=str):
  return _type(sys.stdin.readline().strip())
def input_n(_type=str):
  return list(map(_type, input().split()))

def get_cost(costs, l, r, route, land):
  if r == N-1:
    return costs[N-1] - costs[r+1] + costs[l-1] + land[route[l-1]]
  
  return costs[N-1] - costs[r+1] + costs[l-1] + dists[route[l-1]][route[r+1]] + land[route[l-1]]

def search(costs, l, route, land):
  # lower bound
  srt, end = l, N-1
  
  while srt < end:
    mid = (srt + end) // 2
    c = get_cost(costs, l, mid, route, land)
    if c > R:
      srt = mid + 1
    else:
      end = mid
  return end

N, M, R = input_n(int) 
INF = 10**10
dists = [input_n(int) for _ in range(M)] 
land = input_n(int)
route = [r-1 for r in input_n(int)]

for c in range(M):
  for a in range(M):
    for b in range(M):
      dists[a][b] = min(dists[a][b], dists[a][c] + dists[c][b])
   
cur = 0
costs = [0]*(N+1)
for idx, r in enumerate(route):
  if idx == 0:
    costs[idx] = dists[cur][r]
  else:
    costs[idx] = costs[idx-1] + dists[cur][r]
  cur = r
costs[N] = costs[N-1]

min_cnt, min_c = INF, INF
for r in route:
  c = costs[-1] + land[r]
  if c <= R:
    if 0 < min_cnt:
      min_cnt = 0
      min_c = c
    elif 0 == min_cnt:
      min_c = min(min_c, c)
    
for l in range(1, N):
  r = search(costs, l, route, land)
  c = get_cost(costs, l, r, route, land)
  
  if c > R:
    continue
  
  cnt = r - l + 1
  if cnt < min_cnt:
    min_cnt = cnt
    min_c = c
  elif cnt == min_cnt:
    min_c = min(min_c, c)

if min_cnt == INF:
  print(-1)
else:
  print(min_cnt, min_c)
