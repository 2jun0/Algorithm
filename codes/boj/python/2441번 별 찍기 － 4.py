import sys

def input(type=str):
  return type(sys.stdin.readline().strip())
def input_n(type=str):
  return list(map(type, input().split()))

N = input(int)
for i in range(N):
  print(' '*i + '*'*(N-i))