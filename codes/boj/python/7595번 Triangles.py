import sys
def input(_type=str):
  return _type(sys.stdin.readline().strip())
def input_n(_type=str):
  return list(map(_type, input().split()))

while True:
  x = input(int)
  
  if x == 0:
    break
  
  for k in range(1, x+1):
    print('*'*k)