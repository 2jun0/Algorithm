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

def func(X, Y):
  return 100*Y//X
X, Y = input_n(int)
Z = func(X,Y)
if X == Y:
  print(-1)
else:
  first, end = 1, 10**11
  while first < end:
    mid = (first + end) // 2
    if Z == func(X+mid, Y+mid):
      first = mid+1
    else: end = mid
  print(first if first != 10**11 else -1)