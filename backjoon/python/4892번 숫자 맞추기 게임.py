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

n = input(int)
t = 1
while n != 0:
  n1 = 3*n
  if n1%2 == 0: n2=n1//2
  else: n2=(n1+1)//2
  n3 = 3*n2
  n4 = n3//9

  print('{}. {} {}'.format(t, 'even' if n1%2==0 else 'odd', n4))

  n = input(int)
  t+=1