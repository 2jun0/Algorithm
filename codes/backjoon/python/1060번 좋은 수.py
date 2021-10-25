import sys
INF = 10**20
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))
def print_n(L, join_str=' '):
  for i,l in enumerate(L): print(l, end=join_str if i<len(L)-1 else '\n')
def LL(n,m,d=0): return [[d]*n for _ in range(m)]
def avg(l): return sum(l)/len(l)
def getLRUD(i,j): return [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]

import heapq

L = input(int)
S = input_n(int)
S.sort()
N = input(int)

def get_cnt(x, A, B):
  if A == INF or B == INF: return INF
  return (x-A+1)*(B-x+1) - 1


queue_s = []
visited = []

def queue_add(tx, A, B):
  if A <= tx <= B and tx not in visited:
    visited.append(tx)
    heapq.heappush(queue_s, (get_cnt(tx, A, B), tx, A, B))

for s in S:
  queue_add(s, s, s)

prev = 0
for s in S:
  queue_add(prev+1, prev+1, s-1)
  queue_add(s-1, prev+1, s-1)
  prev = s
queue_add(prev+1, prev+1, INF)

R = []
n = 0
while len(queue_s) > 0 and n < N:
  cnt, x, A, B = heapq.heappop(queue_s)
  R.append(x)

  for tx in [x+1, x-1]:
    queue_add(tx, A, B)

  n += 1

print_n(R)