from collections import defaultdict
import sys
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

INF = 10**8

class UnionFindNode:
  def __init__(self):
    self.p = self
  def find(self):
    if self.p != self:
      self.p = self.p.find()
    return self.p

  def union(self, n):
    n.find().p = self.find()

RED, BLUE = 0, 1
min_diff = INF

def is_chunks_two(graph, colors):
  '''colors를 만족할 때, 청크가 2개인가?'''
  nodes = [UnionFindNode() for _ in range(len(graph))]

  for x in range(len(graph)):
    for nxt in graph[x]:
      if colors[x] == colors[nxt]:
        # 같은 색깔이라면 병합한다.
        nodes[x].union(nodes[nxt])

  parents = set()
  for node in nodes:
    parents.add(node.find())

  # 청크가 2개 인지를 반환한다.
  return len(parents) == 2

def dfs(graph, nums, i, colors, r_v, b_v):
  '''두 구역으로 나눌 수 있는 모든 경우의 수 중, 가장 차이가 작은 값을 춪는다.'''
  global min_diff

  if i == len(graph):
    if is_chunks_two(graph, colors):
      min_diff = min(min_diff, abs(r_v-b_v))
    return

  colors[i] = RED
  dfs(graph, nums, i+1, colors, r_v+nums[i], b_v)
  colors[i] = BLUE
  dfs(graph, nums, i+1, colors, r_v, b_v+nums[i])


N = input(int)
nums = input_n(int)
graph = defaultdict(set)

for x in range(N):
  _inputs = input_n(int)[1:]
  inputs = [v-1 for v in _inputs]

  for y in inputs:
    graph[x].add(y)
    graph[y].add(x)
  graph[x].add(x)

dfs(graph, nums, 0, [-1]*N, 0, 0)
print(min_diff if min_diff != INF else -1)