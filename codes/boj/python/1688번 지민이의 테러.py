import sys
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

def ccw(a, b, c):
  return (c[0]-a[0]) * (b[1]-a[1]) - (c[1]-a[1]) * (b[0]-a[0])

def is_cross(a, b, c, d):
  a, b = min(a,b), max(a,b)
  c, d = min(c,d), max(c,d)
  
  abc = ccw(a,b,c)
  abd = ccw(a,b,d)
  cda = ccw(c,d,a)
  cdb = ccw(c,d,b)
  
  rs = abc * abd <= 0 and cda * cdb <= 0
  if abc * abd == 0 and cda * cdb == 0:
    if d < a or b < c:
      rs = False
  return rs

def is_in(a, b, x):
  a, b = min(a,b), max(a,b)
  
  if ccw(a,b,x) != 0:
    return False
  if a[0] == x[0] and x[0] == b[0]:
    return a[1] <= x[1] <= b[1]
  else:
    return a[0] <= x[0] <= b[0]

N = input(int)
P = [tuple(input_n(int)) for _ in range(N)]
A = [tuple(input_n(int)) for _ in range(3)]
barriers = []
for i in range(N-1):
  barriers.append((P[i], P[i+1]))
barriers.append((P[-1], P[0]))

for a in A:
  c = 0
  
  for bp1, bp2 in barriers:
    if is_in(bp1, bp2, a):
      c = 1
      break
    
    if is_cross(a, (1000000001, a[1]+1), bp1, bp2):
      c += 1
  print(1 if c % 2 == 1 else 0)