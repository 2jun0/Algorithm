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

N, A = input_n(int)

def exeuclid(a, b):
  V = [(1, 0, a), (0, 1, b)] # s, t, r
  while True:
    s1, t1, r1 = V.pop(0)
    s2, t2, r2 = V[-1]
    q2 = r1 // r2
    r3 = r1 - r2*q2
    s3 = s1 - s2*q2
    t3 = t1 - t2*q2
    if r3 == 0:
      while s2 <= 0: s2, t2 = s2 + b, t2 - a
      return s2, t2
    V.append((s3, t3, r3))

from math import gcd
if gcd(A, N) != 1: 
  print_n([N-A,  -1])
else:
  x, y = exeuclid(A, N)
  print_n([N-A,  x])