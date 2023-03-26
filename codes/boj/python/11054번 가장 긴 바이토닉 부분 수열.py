import sys

def input(type=str):
  return type(sys.stdin.readline().strip())
def input_n(type=str):
  return list(map(type, input().split()))

N = input(int)
A = input_n(int)

up = [1]*N
down = [1]*N

for curr in range(N):
  for prev in range(curr):
    if A[curr] > A[prev]:
      up[curr] = max(up[curr], up[prev] + 1)

for curr in range(N-1, -1, -1):
  for prev in range(N-1, curr, -1):
    if A[curr] > A[prev]:
      down[curr] = max(down[curr], down[prev] + 1)

rs = 0
for i in range(N):
  rs = max(rs, up[i] + down[i] - 1)
  
print(rs)