import sys

def input(_type=str):
	return _type(sys.stdin.readline().rstrip())
def input_n(_type):
	return list(map(_type, input().split()))

import heapq
N = input(int)

h = []
for _ in range(N):
  x = input(int)
  if x > 0:
    heapq.heappush(h, x)
  else:
    if len(h) == 0:
      print(0)
    else:
      tmp = heapq.heappop(h)
      print(tmp)
    