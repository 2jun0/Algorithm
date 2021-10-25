import sys
sys.setrecursionlimit(10000000) # 재귀 제한 풀기
INF = 10**8
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))
def print_n(L, join_str=' '):
  for i,l in enumerate(L): print(l, end=join_str if i<len(L)-1 else '\n')
def LL(n,m,d=0): return [[d]*n for _ in range(m)]

N, S = input_n(int)
A = input_n(int)

start, end = 0, 0
s = 0
min_len = INF
while True:
  if s < S:
    if end >= N: break
    s+=A[end]
    end+=1
  elif s >= S:
    min_len = min(min_len, end-start)
    if start >= N: break
    s-=A[start]
    start+=1
    
print(min_len if min_len < INF else 0)