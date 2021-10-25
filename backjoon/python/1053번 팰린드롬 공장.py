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
def getLRUD(i,j): return [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]

S = [c for c in input()]

dp = LL(len(S), len(S), INF)
def reset_dp():
  global dp
  dp = LL(len(S), len(S), INF)

def get_dp_v(i,j):
  if dp[i][j] >= INF:
    if i == j: dp[i][j] = 0
    elif i > j:
      if S[i] == S[j]: dp[i][j] = 0
      else: dp[i][j] = INF
    else:
      cul_dp(i,j)

  return dp[i][j]
    
def cul_dp(i,j):
  dp[i][j] = min(get_dp_v(i+1, j)+1, get_dp_v(i, j-1)+1)

  if S[i] == S[j]:
    dp[i][j] = min(dp[i][j], get_dp_v(i+1, j-1))
  else:
    dp[i][j] = min(dp[i][j], get_dp_v(i+1, j-1)+1)

reset_dp()
min_result = get_dp_v(0, len(S)-1)
for i in range(len(S)):
  for j in range(i+1, len(S)):
    reset_dp()
    S[i], S[j] = S[j], S[i]
    min_result = min(min_result, get_dp_v(0, len(S)-1)+1)
    S[i], S[j] = S[j], S[i]

print(min_result)