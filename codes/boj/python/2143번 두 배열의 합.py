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

T = input(int)
n = input(int)
A = input_n(int)
m = input(int)
B = input_n(int)

sum_A = [A[0]]
for a in A[1:]: sum_A.append(a+sum_A[-1])

sum_B = [B[0]]
for b in B[1:]: sum_B.append(b+sum_B[-1])

bu_sum_A = []
for i in range(n):
  for j in range(i+1):
    bu_sum_A.append(sum_A[i] - sum_A[j] + A[j])
bu_sum_A.sort()

sum_v = 0
for i in range(m):
  for j in range(i+1):
    x = T-(sum_B[i] - sum_B[j] + B[j])
    sum_v += upper_bound(bu_sum_A, x) - lower_bound(bu_sum_A, x)
print(sum_v)