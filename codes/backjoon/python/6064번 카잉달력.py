import sys

def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
  return list(map(_type, input().split()))

# <1,1>
# <2,2>
# <3,3> = <3, 3%4=y%4>

# <1,4>
# <2,1> 
# <3,2> = <3, 6%4=y%4>

# <1,3>
# <2,4>
# <3,1> = <3, 9%4=y%4>

# <1,2>
# <2,3>
# <3,4> = <3, 12%4=y%4>

def get_k(M, N, x, y):
  n = x
  # n = x + Mt
  # <x, n%N=y%N>
  while n <= M*N:
    if n%N == y%N:
      return n

    n += M
  return -1

T = input(int)
for _ in range(T):
  M, N, x, y = input_n(int)
  print(get_k(M,N,x,y))