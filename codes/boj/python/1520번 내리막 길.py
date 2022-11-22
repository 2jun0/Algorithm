import sys
import heapq

def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

M, N = input_n(int)
table = [input_n(int) for _ in range(M)]

# create heapq
hq = []
for y in range(M):
  for x in range(N):
    heapq.heappush(hq, (-table[y][x], y, x))

cnts = [[0]*N for _ in range(M)]
cnts[0][0] = 1

while hq:
  _, y, x = heapq.heappop(hq)
  for ny, nx in [(y-1,x),(y+1,x),(y,x-1),(y,x+1)]:
    if 0<=ny<M and 0<=nx<N and table[y][x] > table[ny][nx]:
      cnts[ny][nx] += cnts[y][x]

print(cnts[-1][-1])
