import sys
sys.setrecursionlimit(10000000) # 재귀 제한 풀기
INF = 10**8
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

N, M = input_n(int)
_A = [input_n(int) for _ in range(N)]
A = [[0]*(M+2) for _ in range(N+2)]
for i, L in enumerate(_A): 
  for j, a in enumerate(L): 
    A[i+1][j+1] = a

N, M = N+2, M+2
exposed = [[False]*M for _ in range(N)]
cnt = [[0]*M for _ in range(N)]
s1 = []
s2 = [(0,0)]
t = 0
while len(s2) > 0:
  s1, s2 = s2, s1
  for i,j in s1: A[i][j] = 0
  while len(s1) > 0:
    i, j = s1.pop()
    if not (0<=i<N and 0<=j<M): continue
    if exposed[i][j]: continue
    if A[i][j] == 1:
      cnt[i][j]+=1
      if cnt[i][j] == 2: s2.append((i,j))
      continue
    exposed[i][j] = True
    T = [(i-1,j), (i+1,j), (i,j-1), (i,j+1)]
    for ti, tj in T:  
      s1.append((ti,tj))
  t+=1
print(t-1)