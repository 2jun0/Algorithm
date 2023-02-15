import sys
sys.setrecursionlimit(100001)
def input(_type=str):
	return _type(sys.stdin.readline().rstrip())
def input_n(_type):
	return list(map(_type, input().split()))

def init_parents(p, dep, x, cost):
  depths[x] = dep
  parents[x][0] = p
  costs[x][0] = cost
  
  for child, d in adj[x]:
    if depths[child] != -1:
      continue
    
    init_parents(x, dep+1, child, d)
    
def update_parents():
  for k in range(1, 20):
    for x in range(1, N+1):
      if parents[x][k-1] != 0:
        parents[x][k] = parents[parents[x][k-1]][k-1]
        costs[x][k] = costs[x][k-1] + costs[parents[x][k-1]][k-1]
  
def find_parent(x, d):
  '''d번째 부모 찾기'''
  p = x
  k = 0
  while d > 0:
    if d % 2 == 1:
      p = parents[p][k]
    k += 1
    d >>= 1
  
  return p
  
def find_LCA(a, b):
  '''최소 공통 부모 찾기
  - returns: 부모, a와의 비용, b와의 비용, a와의 거리, b와의 거리
  '''
  reversed = False
  if depths[a] > depths[b]:
    reversed = True
    a, b = b, a
  
  cost_a = 0
  dist_a = 0
  cost_b = 0
  dist_b = 0

  dep_diff = depths[b] - depths[a]
  k = 0
  while dep_diff > 0:
    if dep_diff % 2 == 1:
      cost_b += costs[b][k]
      dist_b += 2**k
      b = parents[b][k]
      
    k += 1
    dep_diff >>= 1
  
  if a != b:
    '''같은 부모를 찾음'''
    for k in range(19, -1, -1):
      if parents[a][k] != 0 and parents[a][k] != parents[b][k]:
        cost_a += costs[a][k]
        cost_b += costs[b][k]
        
        dist_a += 2**k
        dist_b += 2**k
        
        a = parents[a][k]
        b = parents[b][k]
    
    '''같은 부모로 이동'''
    cost_a += costs[a][0]
    cost_b += costs[b][0]
    dist_a += 1
    dist_b += 1
    a = parents[a][0]
    b = parents[b][0]
    
  if reversed:
    return a, cost_b, cost_a, dist_b, dist_a
  else:
    return a, cost_a, cost_b, dist_a, dist_b

def cmd1(a, b):
  '''a부터 b까지의 비용 찾기'''
  p, cost_a, cost_b, dist_a, dist_b = find_LCA(a, b)
  return cost_a + cost_b

def cmd2(a, b, k):
  '''k번째 경로의 노드 찾기'''
  p, cost_a, cost_b, dist_a, dist_b = find_LCA(a, b)
  
  # a도 경로에 포함되기 때문에 dist_a+1를 해야한다.
  # b도 포함해야 하지만, p가 중복되기 때문에 그대로 둔다.
  dist_a += 1
  
  if dist_a < k:
    # k = dist_a + alpha
    # alpha = k - dist_a
    # 찾야아 할것: b의 dist_b - alpha번째 부모
    # bp = dist_b - alpha
    #    = dist_b - k + dist_a
    return find_parent(b, dist_b - k + dist_a)
  else:
    return find_parent(a, k-1)
  

N = input(int)
adj = [[] for _ in range(N+1)]
parents = [[0]*20 for _ in range(N+1)]
costs = [[0]*20 for _ in range(N+1)]
depths = [-1]*(N+1)

for _ in range(N-1):
  a, b, w = input_n(int)
  adj[a].append((b,w))
  adj[b].append((a,w))
  
init_parents(0, 0, 1, 0)
update_parents()

M = input(int)
for _ in range(M):
  cmds = input_n(int)
  if cmds[0] == 1:
    a, b = cmds[1], cmds[2]
    print(cmd1(a, b))
  if cmds[0] == 2:
    a, b, k = cmds[1], cmds[2], cmds[3]
    print(cmd2(a,b,k))
    
    