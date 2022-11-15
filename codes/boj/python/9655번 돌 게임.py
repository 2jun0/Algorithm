import sys

def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

N = input(int)
turn = 0

while N > 0:
  if N >= 3:
    N-=3
  else:
    N-=1
  
  turn += 1
print('SK' if turn % 2 != 0 else 'CY')