import sys
def input(_type=str):
  return _type(sys.stdin.readline().strip())
def input_n(_type=str):
  return list(map(_type, input().split()))

INF = 10**8
N = input(int)
A = [input_n(int) for _ in range(N)]

A.sort()
d = INF
def get_closest_d(A, l, r):
  global d
  
  def get_dist(a, b):
    return (a[0] - b[0])**2 + (a[1] - b[1])**2
  
  if l >= r:
    return INF
  if l+1 == r: 
    return get_dist(A[l], A[r])
  
  m = (l+r)//2
  # left
  d = min(d, get_closest_d(A, l, m))
  # right
  d = min(d, get_closest_d(A, m+1, r))
  # center (2 pointer)
  
  mids = []
  for i in range(l, r+1):
    if (A[i][0] - A[m][0]) ** 2 < d:
      mids.append(A[i])
    
  mids.sort(key=lambda xy: (xy[1], xy[0]))
  
  for i in range(len(mids)):
    for j in range(i+1, len(mids)):
      dy = (mids[i][1] - mids[j][1]) ** 2
      if dy >= d:
        break
      
      d = min(d, get_dist(mids[i], mids[j]))
      
  return d

print(get_closest_d(A, 0, N-1))