import sys

def input(type=str):
  return type(sys.stdin.readline().strip())
def input_n(type=str):
  return list(map(type, input().split()))

N, M = input_n(int)
if N == M:
  print(1)
else:
  print(0)