import sys

INF = 10**8
def input(_type=str):
	return _type(sys.stdin.readline().rstrip())
def input_n(_type=str):
	return list(map(_type, input().split()))
def print_n(L):
  s = ''
  for l in L: s+='{} '.format(l)
  print(s[:-1])

import heapq

N = input(int)
h = []
for _ in range(N):
  x = input(int)
  if x == 0: 
    if len(h) == 0: print(0)
    else: print(heapq.heappop(h)[1])
  else: heapq.heappush(h, (abs(x), x))
