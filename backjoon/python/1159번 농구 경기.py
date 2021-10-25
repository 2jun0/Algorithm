import sys
sys.setrecursionlimit(10000000) # 재귀 제한 풀기
INF = 10**10
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))
def print_n(L, join_str=' ', end_str='\n'):
  for i,l in enumerate(L): print(l, end=join_str if i<len(L)-1 else end_str)
def LL(n,m,d=0): return [[d]*n for _ in range(m)]

N = input(int)
A = {}
for _ in range(N):
  a = input()[0]
  if a in A.keys():
    A[a] +=1
  else:
    A[a] = 1

B = []
for a, cnt in A.items():
  if cnt >= 5:
    B.append(a)

if len(B) == 0:
  print('PREDAJA')
else:
  B.sort()
  print_n(B,'')
  