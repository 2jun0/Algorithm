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

m, seed, x1,x2 = input_n(int)
flag = False
for a in range(m):
  for c in range(m):
    if x1 == (a*seed+c)%m and x2 == (a*x1+c)%m:
      print(a,c)
      flag = True
      break
  if flag: break