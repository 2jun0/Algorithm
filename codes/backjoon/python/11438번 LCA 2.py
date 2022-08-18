from collections import deque
from math import log, ceil
import sys
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

def init_tree():
  q = deque()

  depths[0] = 0
  # 아래 루틴과 같지만, 코드 간결화를 위해 간단하게 씀.
  for k in range(MAX_K+1):
    parents[0][k] = 0
  q.append(0)

  while q:
    a = q.popleft()
    
    for b in graph[a]:
      if depths[b] == -1:
        depths[b] = depths[a] + 1
        parents[b][0] = a
        for k in range(1, MAX_K+1):
          # 2**k번째 부모 = 2**(k-1)번째 부모의 2**(k-1)번째 부모
          parents[b][k] = parents[parents[b][k-1]][k-1]
        q.append(b)

def get_lca(a, b):
  # a가 더 아래에 있어야 함
  if depths[a] < depths[b]:
    a, b = b, a

  # k 탐색
  k = MAX_K
  while k >= 0 and depths[a] > depths[b]: # a가 b보다 위에 있지 않아야 함!
    # k만큼 이동했을때, b보다 위로 가지 않는가?
    if depths[parents[a][k]] >= depths[b]:
      a = parents[a][k]
    else:
      k = k -1

  # k 탐색
  k = MAX_K
  # 최소 공통 부모 바로 아래에 a와 b가 있어야 함
  # a != b여야 한다. 
  # 만약 a == b라면... 그대로 a를 반환
  if a == b:
    return a
  
  while k >= 0:
    if parents[a][k] != parents[b][k]:
      a = parents[a][k]
      b = parents[b][k]  
    else:
      k = k-1
  
  return parents[a][0]

N = input(int)
graph = [[] for _ in range(N)]
depths = [-1]*N
# i번째 노드의 2**k번째 부모
# 부모는 최대 N-1번째 까지 있을 수 있으므로
# 2**K <= N-1, K <= log(N-1,2), K <= ceil(log(N-1,2)), K < ceil(log(N-1,2))+1
MAX_K = ceil(log(N-1,2)) 
parents = [[-1 for k in range(MAX_K+1)] for _ in range(N)]

for _ in range(N-1):
  a, b = input_n(int)
  a, b = a-1, b-1

  graph[a].append(b)
  graph[b].append(a)

init_tree()

M = input(int)

for _ in range(M):
  a, b = input_n(int)
  a, b = a-1, b-1

  print(get_lca(a, b)+1)