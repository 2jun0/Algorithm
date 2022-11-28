import sys

def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

T = input(int)
for _ in range(T):
  lt, wt, le, we = input_n(int)
  
  A = lt*wt
  B = le*we
  if A > B:
    print('TelecomParisTech')
  elif A < B:
    print('Eurecom')
  else:
    print('Tie')