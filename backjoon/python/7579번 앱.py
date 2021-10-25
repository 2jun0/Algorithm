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

N, M = input_n(int)
am = input_n(int)
ac = input_n(int)
A = [(m, c) for m, c in zip(am, ac)]

dp1 = [0]*10001 # memory[cost]
dp2 = [0]*10001 # memory[cost]

for m, c in A:
  for i in range(10001):
    dp1[i] = dp2[i]
  for kc in range(c, 10001):
    dp2[kc] = max(dp1[kc], dp1[kc-c] + m)

for i, m in enumerate(dp2):
  if m >= M:
    print(i)
    break