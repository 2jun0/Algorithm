from collections import deque
import sys
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

def init_depths():
  srt_q = deque()

  depths[0] = 0
  parents[0] = 0
  srt_q.append(0)

  while srt_q:
    srt = srt_q.popleft()

    for end in graph[srt]:
      if depths[end] == -1:
        depths[end] = depths[srt] + 1
        parents[end] = srt
        srt_q.append(end)

def get_LCA(a, b):
  # a가 b보다 더 아래여야 함 (depths[a] >= depths[b])
  if depths[a] < depths[b]:
    a, b = b, a

  while depths[a] > depths[b]:
    a = parents[a]

  while a != b:
    a = parents[a]
    b = parents[b]

  return a

N = input(int)

graph = [[] for _ in range(N)]
depths = [-1]*N
parents = [-1]*N

for _ in range(N-1):
  a, b = input_n(int)
  a, b = a - 1, b - 1
  graph[a].append(b)
  graph[b].append(a)

init_depths()

M = input(int)
for _ in range(M):
  a, b = input_n(int)
  a, b = a - 1, b - 1

  print(get_LCA(a, b)+1)