import sys

def input(_type=str):
  return _type(sys.stdin.readline().strip())
def input_n(_type=str):
  return list(map(_type, input().split()))

N = input(int)
costs = {}
for _ in range(N):
  X, T, C = input_n(int)
  costs[T-X] = costs.setdefault(T-X, 0) + C
  
print(max(costs.values()))
