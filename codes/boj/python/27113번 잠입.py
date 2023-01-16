import sys
def input(_type=str):
  return _type(sys.stdin.readline().strip())
def input_n(_type=str):
  return list(map(_type, input().split()))

N, M = input_n(int)
px = 0
flag = True

for y in range(N-1):
  cmds = input_n(str)
  c = int(cmds[0])
  
  if c == 0:
    continue
  
  sx = M
  ex = -1
  for i in range(c):
    x = int(cmds[1+i*2]) - 1
    d = cmds[1+i*2+1]
    if d == 'R':
      sx = min(sx, x)
    if d == 'L':
      ex = max(ex, x)
  if sx == M:
    sx = 0
  if ex == -1:
    ex = M-1
  
  # move
  ls = []
  if sx > ex:
    ls = [(0, ex), (sx, M-1)]
  else:
    ls = [(sx, ex)]
  
  for ssx, eex in ls:
    if ssx <= px <= eex:
      px = eex+1
      
    if px >= M:
      flag = False

if flag:
  print("YES")
else:
  print("NO")