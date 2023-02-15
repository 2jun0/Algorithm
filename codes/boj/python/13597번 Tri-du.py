import sys

def input(type=str):
  return type(sys.stdin.readline().strip())
def input_n(type=str):
  return list(map(type, input().split()))

A, B = input_n(int)
print(max(A,B))