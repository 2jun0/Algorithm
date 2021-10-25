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

S = input()
N = input(int)
A = [input() for _ in range(N)]
sorted_A = {a:sorted(a) for a in A}

dp = [INF]*(len(S)+1)
dp[0] = 0
for s_end in range(len(S)+1):
  for a in A:
    if len(a) <= s_end:
      s_start = s_end - len(a)

      # check chars
      flag = True
      sorted_S = sorted(S[s_start:s_end])
      sorted_a = sorted_A[a]
      for i in range(len(sorted_S)):
        if sorted_a[i] != sorted_S[i]:
          flag = False
          break
      
      if flag:
        cost = 0
        for i in range(len(a)):
          if S[s_start+i] != a[i]:
            cost+=1
        if s_end == 0:
          dp[s_end] = min(dp[s_end], cost)
        else:
          dp[s_end] = min(dp[s_end], cost + dp[s_start])

if dp[-1] == INF:
  print(-1)
else:
  print(dp[-1])