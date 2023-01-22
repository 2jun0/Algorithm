import sys

def input(_type=str):
  return _type(sys.stdin.readline().strip())
def input_n(_type=str):
  return list(map(_type, input().split()))

A, B = input_n(int)
M = (B - A) / 400
print(1/(1+10**M))