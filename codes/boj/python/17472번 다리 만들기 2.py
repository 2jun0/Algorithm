from collections import defaultdict, deque
import sys
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

INF = 10**8

def map_table(N, M, table):
  '''table에 개별 섬들에 서로 다른 값을 매핑함'''

  def map_chunk(visited, sy,sx,v):
    '''(sy,sx)에 연결된 타일의 값을 v로 매핑함'''
    q = deque()
    q.append((sy,sx))

    while q:
      y,x = q.popleft()
      table[y][x] = v

      for ny, nx in [(y+1,x),(y-1,x),(y,x+1),(y,x-1)]:
        if 0<=ny<N and 0<=nx<M and not visited[ny][nx] and table[ny][nx] != 0:
          visited[ny][nx] = True
          q.append((ny,nx))

  visited = [[False]*M for _ in range(N)]

  v = 1
  for y in range(N):
    for x in range(M):
      if not visited[y][x] and table[y][x] != 0:
        map_chunk(visited,y,x,v)
        v += 1

def get_chunk_count(table):
  vs = set()
  for line in table:
    vs.update(line)
  return len(vs)-1

def create_graph(N, M, table):
  '''섬 별 거리 그래프를 만들어서 반환'''
  def update_graph(graph, sy, sx):
    '''(sy,sx)부터 다른 섬까지의 거리로 그래프를 업데이트 함'''
    src_v = table[sy][sx]

    costs = [[-1]*M for _ in range(N)]
    q = deque()
    
    costs[sy][sx] = 0
    q.append((sy,sx,-1,0))
    q.append((sy,sx,1,0))
    q.append((sy,sx,0,-1))
    q.append((sy,sx,0,1))

    while q:
      y, x, dy, dx = q.popleft()

      dst_v = table[y][x]
      if dst_v not in [src_v, 0]:
        if costs[y][x]-1 > 1:
          graph[src_v][dst_v] = min(graph[src_v][dst_v], costs[y][x]-1)
        continue
      
      if dst_v == 0 or (y,x) == (sy,sx):
        ny, nx = y + dy, x + dx
        if 0<=ny<N and 0<=nx<M and costs[ny][nx] == -1:
          costs[ny][nx] = costs[y][x] + 1
          q.append((ny,nx,dy,dx))

  graph = {
    x: defaultdict(lambda: INF)
    for x in range(1, get_chunk_count(table)+1)
  }

  for y in range(N):
    for x in range(M):
      if table[y][x] != 0:
        update_graph(graph, y, x)
  
  return graph

def get_travel_min_dist(graph):
  '''그래프 방문 최소 경로 구하기'''
  class Node:
    def __init__(self):
      self.p = self
    def find(self):
      if self.p != self:
        self.p = self.p.find()
      return self.p
    def union(self, n):
      n.find().p = self.find()

  # (dist, src, dst)
  lines = []
  for src in graph:
    for dst, dist in graph[src].items():
      lines.append((dist, src, dst))

  lines.sort()

  sum_dist = 0

  nodes = [Node() for _ in range(len(graph)+1)]
  for dist, src, dst in lines:
    if nodes[src].find() != nodes[dst].find():
      nodes[src].union(nodes[dst])
      sum_dist += dist

  for x in range(1, len(graph)+1):
    if nodes[1].find() != nodes[x].find():
      return -1

  return sum_dist

N, M = input_n(int)
table = [input_n(int) for _ in range(N)]

map_table(N, M, table)
graph = create_graph(N, M, table)

print(get_travel_min_dist(graph))