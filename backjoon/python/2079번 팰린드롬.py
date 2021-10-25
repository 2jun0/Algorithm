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

S = input()
N = len(S)

is_FD = [[None]*N for _ in range(N)]
for x in range(N):
  is_FD[x][x] = True
for x in range(N-1):
  if S[x] == S[x+1]:
    is_FD[x][x+1] = True
  else:
    is_FD[x][x+1] = False

for i in range(1,(N-1)//2+1): # 반지름
  for x in range(i, N-i):
    if is_FD[x-i+1][x+i-1] and S[x-i] == S[x+i]:
      is_FD[x-i][x+i] = True
    else:
      is_FD[x-i][x+i] = False
for i in range(1,N//2):
  for x in range(i, N-i-1):
    if is_FD[x-i+1][x+i] and S[x-i] == S[x+i+1]:
      is_FD[x-i][x+i+1] = True
    else:
      is_FD[x-i][x+i+1] = False

cnts = [INF]*N
for j in range(N):
  if is_FD[0][j]:
    cnts[j] = 1
for i in range(1,N):
  for j in range(i,N):
    if is_FD[i][j]:
      cnts[j] = min(cnts[j],cnts[i-1]+1)
print(cnts[-1])