import sys
def input(_type=str):
  return _type(sys.stdin.readline().strip())
def input_n(_type=str):
  return list(map(_type, input().split()))

N = input(int)
A = [input_n(int) for _ in range(N)]
A.sort()

flag = True
x = 1
y = 1
for d, t in A:
  
  while t > 0:
    while x % 7 in [6, 0]:
      x += 1
    
    if x <= d:
      x += 1
      t -= 1
    elif y <= d:
      y += 1
      t -= 1
    else:
      flag = False
      break
  
  if not flag:
    break
if flag:
  print(y-1)
else:
  print(-1)