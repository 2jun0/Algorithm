import sys
import heapq

def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

N = input(int)
h = []

info = []

for _ in range(N):
  t, s = input_n(int)
  info.append((t,s))

info.sort()
for t, s in info:
  if h and h[0] <= t:
    heapq.heappop(h)
    heapq.heappush(h, s)
  else:
    heapq.heappush(h, s)

print(len(h))