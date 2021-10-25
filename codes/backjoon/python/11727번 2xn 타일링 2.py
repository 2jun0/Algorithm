import sys

INF = 10**8
def input(_type=str):
	return _type(sys.stdin.readline().rstrip())
def input_n(_type=str):
	return list(map(_type, input().split()))
def print_n(L):
  s = ''
  for l in L: s+='{} '.format(l)
  print(s[:-1])

n = input(int)
A = [0]*1000
A[0], A[1] = (1, 3)
for i in range(2, n):
  # 가로 두개 + 정사각형 하나 + 세로 하나
  A[i] = (A[i-2]+A[i-2]+A[i-1]) % 10007
print(A[n-1])
