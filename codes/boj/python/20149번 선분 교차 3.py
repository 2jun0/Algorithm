import sys
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

# 해가 많은 경우
MANY = 'MANY'

class vector:
  def __init__(self, x, y):
    self.x = x
    self.y = y
  
  def cross(self, other):
    # 외적 
    return self.x*other.y - self.y*other.x
  
  def __mul__(self, v):
    return vector(self.x*v, self.y*v)
  
  def __sub__(self, other) -> "vector":
    return vector(self.x-other.x, self.y-other.y)
  
  def __add__(self, other) -> "vector":
    return vector(self.x+other.x, self.y+other.y)
  
  def __lt__(self, other):
    if self.x != other.x:
      return self.x < other.x
    else:
      return self.y < other.y
  
  def __eq__(self, other):
    return self.x == other.x and self.y == other.y
  
  def __str__(self):
    return str((self.x, self.y))

def intersection(a:vector, b:vector, c:vector, d:vector):
  # 선분 ab와 선분 cd의 교차점을 구함
  # 벡터 ax = x - a = a + pv (p는 상수)
  # 벡터 cx = x - c = c + qw (q는 상수)
  # v = b-a
  # w = d-c
  # (생략) 이해 못함
  # p = (c - a) X w / (v X w)
  # p = (c - a) X (d-c) / ((b-a) X (d-c))
  # x = a + pv = a + ((c - a) X (d-c) / ((b-a) X (d-c))) * (b-a)
  det = (b-a).cross(d-c) 
  x = a + (b-a)*((c-a).cross(d-c) / det)
  return x

def ccw(a: vector, b: vector, c: vector):
  return (b-a).cross(c-a)

def is_parallel(a: vector, b: vector, c: vector, d: vector):
  return (b-a).cross(d-c) == 0

def parallel(a: vector, b: vector, c: vector, d: vector):
  if ccw(a, b, c) != 0:
    # 같은 직선에 놓여있지 않음
    return None
    
  if d < a or b < c:
    # 서로 만나지 않음
    return None
  
  if a == d:
    return a
  if b == c:
    return b
  
  return MANY

def has_intersection(a: vector, b: vector, c: vector, d: vector):
  return ccw(a,b,c) * ccw(a,b,d) <= 0 and ccw(c,d,a) * ccw(c,d,b) <= 0

def solve(a: vector, b: vector, c: vector, d: vector):
  if has_intersection(a,b,c,d):
    if is_parallel(a,b,c,d):
      return parallel(a, b, c, d)

    x = intersection(a, b, c, d)
    return x
  
  return None

L = input_n(int)
a, b = vector(L[0], L[1]), vector(L[2], L[3])
a, b = min(a,b), max(a,b)
L = input_n(int)
c, d = vector(L[0], L[1]), vector(L[2], L[3])
c, d = min(c,d), max(c,d)

x = solve(a, b, c, d)
if x:
  print(1)
  if x is not MANY:
    print(x.x, x.y) 
else: 
  print(0)