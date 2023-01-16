import sys
def input(_type=str):
  return _type(sys.stdin.readline().strip())
def input_n(_type=str):
  return list(map(_type, input().split()))

N = input(int)
V = [False]*200_001
cnt = 0
for _ in range(N):
  a, b = input_n(int)
  if b == 0:
    if not V[a]:
      cnt += 1
      
    V[a] = False
  if b == 1:
    if V[a]:
      cnt += 1
      
    V[a] = True
    
print(cnt + V.count(True))