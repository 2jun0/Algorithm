import sys
sys.setrecursionlimit(10000000) # 재귀 제한 풀기
INF = 10**10
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))
def print_n(L, join_str=' '):
  for i,l in enumerate(L): print(l, end=join_str if i<len(L)-1 else '\n')
def LL(n,m,d=0): return [[d]*n for _ in range(m)]
def avg(l): return sum(l)/len(l)

L = input_n(int)
L1 = [(L[0], L[1], 1), (L[2], L[3], 1)]
L = input_n(int)
L2 = [(L[0], L[1], 1), (L[2], L[3], 1)]

def cp(A, B):
  return (A[1]*B[2] - A[2]*B[1], A[2]*B[0] - A[0]*B[2], A[0]*B[1] - A[1]*B[0])

V = cp(cp(L1[0], L1[1]), cp(L2[0], L2[1]))
# print(V)
if V[2] == 0:
  if V[0] == 0 and V[1] == 0:
    flag = False
    for x, y in [(L2[0][0], L2[0][1]), (L2[1][0], L2[1][1])]:
      for x1, x2, y1, y2 in [(L1[0][0], L1[1][0], L1[0][1], L1[1][1])]:
        if x1 <= x <= x2 and y1 <= y <= y2: flag = True
        if x2 <= x <= x1 and y2 <= y <= y1: flag = True
    for x, y in [(L1[0][0], L1[0][1]), (L1[1][0], L1[1][1])]:
      for x1, x2, y1, y2 in [(L2[0][0], L2[1][0], L2[0][1], L2[1][1])]:
        if x1 <= x <= x2 and y1 <= y <= y2: flag = True
        if x2 <= x <= x1 and y2 <= y <= y1: flag = True
    if flag: print(1)
    else: print(0)
  else: print(0)
else:
  V = (V[0]/V[2], V[1]/V[2])
  
  L1flag, L2flag = False, False
  for x1, x2, y1, y2 in [(L1[0][0], L1[1][0], L1[0][1], L1[1][1])]:
    if min(x1, x2) <= V[0] <= max(x1, x2) and min(y1, y2) <= V[1] <= max(y1, y2): L1flag = True
  for x1, x2, y1, y2 in [(L2[0][0], L2[1][0], L2[0][1], L2[1][1])]:
    if min(x1, x2) <= V[0] <= max(x1, x2) and min(y1, y2) <= V[1] <= max(y1, y2): L2flag = True
  # print(L1flag, L2flag, V, L2[0][0]<=V[0]<=L2[1][0], L2[0][1]<=V[1]<=L2[1][1])
  if L1flag and L2flag: print(1)
  else: print(0)