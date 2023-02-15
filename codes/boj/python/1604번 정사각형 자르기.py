import sys
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

def ccw(a, b, c):
  return (b[0]-a[0])*(c[1]-a[1]) - (b[1]-a[1])*(c[0]-a[0])

def intersection(a,b,c,d):    
  a,b = min(a,b), max(a,b)
  c,d = min(c,d), max(c,d)
  
  s = ((b[0]-a[0])*(a[1]-c[1]) - (b[1]-a[1])*(a[0]-c[0])) / ((d[1]-c[1])*(b[0]-a[0]) - (d[0]-c[0])*(b[1]-a[1]))
  x = c[0]+s*(d[0]-c[0])
  y = c[1]+s*(d[1]-c[1])
  return x,y

def is_cross(a, b, c, d):
  '''평행한것 안됨'''
  a,b = min(a,b), max(a,b)
  c,d = min(c,d), max(c,d)
  
  abc = ccw(a,b,c)
  abd = ccw(a,b,d)
  cda = ccw(c,d,a)
  cdb = ccw(c,d,b)
  
  if abc * abd == 0 and cda * cdb == 0:
    return False

  return abc * abd <= 0 and cda * cdb <= 0

def in_range(a):
  return -10<a[0]<10 and -10<a[1]<10

def crossed_sqaure(a,b):
  inters = set()
  for c, d in [((-10,10),(10,10)), ((-10,-10),(10,-10)), ((-10,-10),(-10,10)), ((10,-10),(10,10))]:  
    if is_cross(a,b,c,d):
      x = intersection(a,b,c,d)
      inters.add(x)
  
  meet_vertex = 0
  meet_line = 0
  for x in inters:
    if x in [(-10,-10), (-10,10), (10,-10), (10,10)]:
      meet_vertex += 1
    else:
      meet_line += 1
        
  return meet_vertex >= 2 or meet_line >= 1

N = input(int)
L = []
for _ in range(N):
  ax,ay,bx,by = input_n(int)
  a, b = (ax,ay), (bx,by)
  if crossed_sqaure(a,b):
    L.append((a,b))

rs = 1
for i in range(len(L)):
  a, b = L[i]
  rs += 1
  for j in range(i+1, len(L)):
    c, d = L[j]
    
    if is_cross(a,b,c,d) and in_range(intersection(a,b,c,d)):
      rs += 1
print(rs)