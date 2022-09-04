from collections import deque
import sys
def input(_type=str):
  return _type(sys.stdin.readline().strip())
def input_n(_type=str):
  return list(map(_type, input().split()))

def init_parents():
  q = deque()

  parents[0] = 0
  depths[0] = 0
  q.append(0)

  while q:
    srt = q.popleft()

    for end in graph[srt]:
      if depths[end] == -1:
        parents[end] = srt
        depths[end] = depths[srt]+1
        q.append(end)

def get_dist(a, b):
  # assert depths[a] >= depths[b]
  # a가 b보다 더 낮은 위치에 있음
  if depths[a] < depths[b]:
    a, b = b, a

  dist = 0
  while depths[a] > depths[b]:
    dist += dists[a][parents[a]]
    a = parents[a]

  while a != b:
    dist += dists[a][parents[a]] + dists[b][parents[b]]
    a = parents[a]
    b = parents[b]

  return dist

N = input(int)

graph = [[] for _ in range(N)]
dists = [{} for _ in range(N)]
parents = [-1]*N
depths = [-1]*N

for _ in range(N-1):
  a, b, d = input_n(int)
  a, b = a-1, b-1
  dists[a][b] = d
  graph[a].append(b)
  dists[b][a] = d
  graph[b].append(a)

init_parents()

M = input(int)

for _ in range(M):
  a, b = input_n(int)
  a, b = a-1, b-1
  print(get_dist(a, b))