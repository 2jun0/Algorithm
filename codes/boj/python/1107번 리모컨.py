import sys

INF = 10**8
def input(_type=str):
	return _type(sys.stdin.readline().rstrip())
def input_n(_type=str):
	return list(map(_type, input().split()))

N_str = input()
N = int(N_str)
M = input(int)
B = input_n(int)
A = [x for x in range(0,10) if x not in B]


def p(x):
  """x를 누를 수 있는가"""
  if x == 0 and x in B: return False
  while x > 0:
    a, x = x%10, x//10
    if a in B: return False
  return True

min_gap = INF

min_x = -1
for x in range(0, 1000001):
  if p(x):
    gap = abs(x-N)
    if min_gap > gap:
      min_gap = gap
      min_x = x

print(min(abs(N-100), len(str(min_x))+min_gap))
