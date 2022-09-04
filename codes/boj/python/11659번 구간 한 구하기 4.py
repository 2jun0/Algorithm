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

N, M = input_n(int)
A = input_n(int)
S = [A[0]]
for a in A[1:]: S.append(S[-1]+a)
for _ in range(M):
  a,b = input_n(int)
  a,b = a-1, b-1

  print(S[b] - S[a] + A[a])