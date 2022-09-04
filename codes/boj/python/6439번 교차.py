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
def ck_cross(A, B, C, D):
	ccw_ab = ccw(A, B, C) * ccw(A, B, D)
	ccw_cd = ccw(C, D, A) * ccw(C, D, B)

	if ccw_ab == 0 and ccw_cd == 0:
		return min(A, B) <= min(C, D) <= max(A, B) \
			or min(C, D) <= min(A, B) <= max(C, D)
	else: return ccw_ab <= 0 and ccw_cd <= 0

T = input(int)
for _ in range(T):
  x_st, y_st, x_ed, y_ed, x_le, y_to, x_ri, y_bo = input_n(int)
  x_le, x_ri = min(x_le, x_ri), max(x_le, x_ri)
  y_bo, y_to = min(y_bo, y_to), max(y_bo, y_to)
  A, B = (x_st, y_st), (x_ed, y_ed)
  C1, D1 = (x_le, y_to), (x_ri, y_to)
  C2, D2 = (x_le, y_bo), (x_ri, y_bo)
  C3, D3 = (x_le, y_to), (x_le, y_bo)
  C4, D4 = (x_ri, y_to), (x_ri, y_bo)
  
  flag = False
  for C, D in [(C1,D1),(C2,D2),(C3,D3),(C4,D4)]:
    if ck_cross(A,B,C,D): flag = True; break
  
  if (x_le <= x_st <= x_ri and y_bo <= y_st <= y_to)\
    or (x_le <= x_ed <= x_ri and y_bo <= y_ed <= y_to):
    flag = True
  
  if flag: print('T')
  else: print('F')