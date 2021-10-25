import sys
INF = 10**10
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))
def print_n(L, join_str=' '):
  for i,l in enumerate(L): print(l, end=join_str if i<len(L)-1 else '\n')
def LL(n,m,d=0): return [[d]*n for _ in range(m)]
def avg(l): return sum(l)/len(l)

def ccw(A, B, C):
	tmp = A[0]*B[1]+B[0]*C[1]+C[0]*A[1] - (A[1]*B[0]+B[1]*C[0]+C[1]*A[0])
	if tmp > 0: return 1
	elif tmp == 0: return 0
	else: return -1

def cross_v(A, B):
  return (A[1]*B[2] - A[2]*B[1], A[2]*B[0] - A[0]*B[2], A[0]*B[1] - A[1]*B[0])

def ck_cross(A, B, C, D):
  ccw_ab = ccw(A, B, C) * ccw(A, B, D)
  ccw_cd = ccw(C, D, A) * ccw(C, D, B)

  V = cross_v(cross_v([A[0],A[1],1],[B[0],B[1],1]), cross_v([C[0],C[1],1],[D[0],D[1],1]))
  # 평행함
  if V[2] == 0:
    # 겹쳐있음
    if ccw_ab==0 and ccw_cd==0:
      # C나 D에서 한점 만남
      if max(A,B) == min(C,D) or min(A,B) == max(C,D):
        return 0.5
      # 여러점 겹쳐있음
      elif (min(A, B) <= min(C, D) <= max(A, B)\
      or min(C, D) <= min(A, B) <= max(C, D)): return INF
      # 겹쳐있지 않음
      else: return 0
    # 평행함
    else: return 0
  # 평행하지 않음
  else:
    # 한점 이상 만남
    if ccw_ab <= 0 and ccw_cd <= 0:
      V = [V[0]/V[2], V[1]/V[2]] # 만나는 점
      # C, D에서 만남
      for X in [C,D]:
        if V[0] == X[0] and V[1] == X[1]: return 0.5
      # 나머지 크로스
      return 1
    # 안 만남
    else: return 0

T = input(int)
for _ in range(T):
  x_min,y_min,x_max,y_max = input_n(int)
  x1,y1,x2,y2 = input_n(int)
  A,B = (x1,y1),(x2,y2)
  LB,LT,RB,RT = (x_min,y_min),(x_min,y_max),(x_max,y_min),(x_max,y_max)

  sum_v = 0
  for C, D in [(LB,LT),(LB,RB),(LT,RT),(RB,RT)]:
    v = ck_cross(A,B,C,D)
    sum_v += v
  if sum_v >= INF: print(4)
  else: print(int(sum_v))