import sys
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

N = input(int)
A = input_n(int)
S = input(int)


for i in range(len(A)):
  B = [(-A[ti],ti) for ti in range(i,len(A))]
  B.sort()
  for _, b_i in B:
    if b_i-i <= S:
      S-= b_i - i
      A = A[:i] + [A[b_i]] + A[i:b_i] + A[b_i+1:]
      break
print_n(A)