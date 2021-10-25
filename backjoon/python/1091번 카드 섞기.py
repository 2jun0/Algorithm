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

N = input(int)
P = input_n(int)
S = input_n(int)

A = [a for a in range(N)]
new_A = [-1]*N
cnt = 0

for _ in range(1000000):
  # match
  match = True
  for i, a in enumerate(A):
    if i%3 != P[a]:
      match = False
      break

  if match: break

  for i, a in enumerate(A):
    new_A[S[i]] = a
  A, new_A = new_A, A
  cnt+=1
if match:
  print(cnt)
else:
  print(-1)