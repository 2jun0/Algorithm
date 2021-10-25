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
is_FD = LL(N, N, False)
for x in range(N): 
  is_FD[x][x] = True
for x in range(N-1): 
  is_FD[x][x+1] = S[x] == S[x+1]

# X0X
for r in range(1,(N+1)//2):
  for x in range(N-r):
    is_FD[x-r][x+r] = is_FD[x-r+1][x+r-1] and S[x-r] == S[x+r]
# XX(XO-X)
for r in range(1,N//2):
  for x in range(N-r-1):
    is_FD[x-r][x+r+1] = is_FD[x-r+1][x+r] and S[x-r] == S[x+r+1]

DP = [INF]*N
DP[0] = 1
for x in range(1,N):
  for y in range(x+1):
    if is_FD[y][x]:
      if y > 0: 
        DP[x] = min(DP[x], DP[y-1]+1)
      else: DP[x] = 1
print(DP[N-1])