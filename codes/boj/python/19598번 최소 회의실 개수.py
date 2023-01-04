import sys
import heapq

def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

n = input(int)
A = []
for _ in range(n):
  A.append(input_n(int))
A.sort()

h = [-1]
for from_t, to_t in A:
  x = heapq.heappop(h)
  if from_t < x:
    heapq.heappush(h, x)
  heapq.heappush(h, to_t)

print(len(h))