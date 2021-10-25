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

def lower_bound(A, x):
  start, end = 0, len(A)
  while start < end:
    mid = (start + end)//2
    if x <= A[mid]:
      end = mid
    else:
      start = mid+1
  return start
def upper_bound(A, x):
  start, end = 0, len(A)
  while start < end:
    mid = (start + end)//2
    if x < A[mid]:
      end = mid
    else:
      start = mid+1
  return start

N, M = input_n(int)
A = [input_n(int) for _ in range(N)]

sum_A = [[0]*M for _ in range(N)]
for y in range(0, N):
  for x in range(0, M):
    if x > 0: sum_A[y][x] += sum_A[y][x-1]
    if y > 0: sum_A[y][x] += sum_A[y-1][x]
    if x > 0 and y > 0: sum_A[y][x] -= sum_A[y-1][x-1]
    sum_A[y][x] += A[y][x]


K = input(int)
for _ in range(K):
  j,i,y,x = input_n(int)
  i,j,x,y = i-1,j-1,x-1,y-1
  sum_v = sum_A[y][x]

  if i > 0: sum_v -= sum_A[y][i-1]
  if j > 0: sum_v -= sum_A[j-1][x]
  if i > 0 and j > 0: sum_v += sum_A[j-1][i-1]
  print(sum_v)