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

X, Y, D, T = input_n(int)
P = (X**2 + Y**2) ** 0.5
K = int(P/D)
a = P-K*D

min_time = INF
min_time = min(min_time, P)
min_time = min(min_time, K*T+a)
min_time = min(min_time, (K+1)*T+(D-a))
if K > 0: min_time = min(min_time, (K+1)*T)
else: min_time = min(min_time, 2*T)
print(min_time)