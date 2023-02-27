import sys
from collections import deque

def input(type=str):
  return type(sys.stdin.readline().strip())
def input_n(type=str):
  return list(map(type, input().split()))

N, L = input_n(int)
A = input_n(int)
window = deque()
D = []

for i in range(N):
  while window and window[-1][0] > A[i]:
    window.pop()
  
  while window and i - window[0][1] >= L:
    window.popleft()
  
  window.append([A[i], i])
  D.append(window[0][0])

print(*D)