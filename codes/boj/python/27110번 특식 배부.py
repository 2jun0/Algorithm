import sys
def input(_type=str):
  return _type(sys.stdin.readline().strip())
def input_n(_type=str):
  return list(map(_type, input().split()))

N = input(int)
A, B, C = input_n(int)

print(min(N, A) + min(N, B)+ min(N, C))