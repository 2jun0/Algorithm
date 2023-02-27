import sys
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

def ccw(a, b, c):
  v = (b[0]-a[0])*(c[1]-a[1]) - (c[0]-a[0])*(b[1]-a[1])
  if v < 0: return -1
  elif v == 0: return 0
  else: return 1
  
L = input_n(int)
A, B = (L[0], L[1]), (L[2], L[3])
A, B = min(A, B), max(A, B)
L = input_n(int)
C, D = (L[0], L[1]), (L[2], L[3])
C, D = min(C, D), max(C, D)
abc = ccw(A, B, C)
abd = ccw(A, B, D)
cda = ccw(C, D, A)
cdb = ccw(C, D, B)

flag = abc * abd <= 0 and cda * cdb <= 0

if abc * abd == 0 and cda * cdb == 0:
  # 평행
  if D < A or B < C:
    flag = False

print(1 if flag else 0)