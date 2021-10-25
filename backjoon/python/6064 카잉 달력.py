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
def lcm(a,b):
  from math import gcd
  return a*b // gcd(a,b)

T = input(int)
for _ in range(T):
  M, N, X, Y = input_n(int)
  if M<N: M, N, X, Y = N, M, Y, X
  if X==M: X=0
  if Y==N: Y=0

  x, y, k = X, X%N, X
  for _ in range(M):
  # while k <= lcm(N,M):
    if y == Y:
      print(k)
      break
    k+=M
    y = (y+M)%N
  else:
    print(-1)