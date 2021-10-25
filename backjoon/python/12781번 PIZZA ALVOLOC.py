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

	return ccw_ab < 0 and ccw_cd < 0

x1,y1,x2,y2,x3,y3,x4,y4 = input_n(int)
A = (x1,y1)
B = (x2,y2)
C = (x3,y3)
D = (x4,y4)

if ck_cross(A,B,C,D): print(1)
else: print(0)