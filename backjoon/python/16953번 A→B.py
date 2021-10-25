import sys
sys.setrecursionlimit(10000000) # 재귀 제한 풀기
INF = 10**8
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))
def print_n(L, join_str=' '):
  for i,l in enumerate(L): print(l, end=join_str if i<len(L)-1 else '\n')

A, B = input_n(int)

import heapq
h = [(1,-A)]
min_d = -1
while len(h) > 0:
  d,x = heapq.heappop(h)
  x = -x
  if B == x: 
    min_d = d
    break
  if B < x: continue
  
  heapq.heappush(h, (d+1, -(x*10+1)))
  heapq.heappush(h, (d+1, -(x*2)))
print(min_d)