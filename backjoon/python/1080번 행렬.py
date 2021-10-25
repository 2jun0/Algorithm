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

N, M = input_n(int)
A, B = [], []
for _ in range(N):
  L = input()
  A.append([])
  for l in L:
    A[-1].append(l)
for _ in range(N):
  L = input()
  B.append([])
  for l in L:
    B[-1].append(l)

def func(i,j):
  for ti in range(i,i+3):
    for tj in range(j,j+3):
      A[ti][tj] = '1' if A[ti][tj] == '0' else '0'

cnt = 0
for i in range(N-2):
  for j in range(M-2):
    if A[i][j] != B[i][j]: 
      func(i,j)
      cnt+=1

flag = True
for i in range(N):
  for j in range(M):
    if A[i][j] != B[i][j]: 
      flag = False
      break
  if not flag: break

if flag: print(cnt)
else: print(-1)