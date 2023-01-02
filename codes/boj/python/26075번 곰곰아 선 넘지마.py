import sys

def input(_type=str):
  return _type(sys.stdin.readline().strip())
def input_n(_type=str):
  return list(map(_type, input().split()))

N, M = input_n(int)
S = input(str)
T = input(str)

one_of_S = []
for i, c in enumerate(S):
  if c == '1':
    one_of_S.append(i)
    
one_of_T = []
for i, c in enumerate(T):
  if c == '1':
    one_of_T.append(i)
    
Z = 0
for si, ti in zip(one_of_S, one_of_T):
  Z += abs(si-ti)
if (Z*Z) % 2 == 0:
  print(Z*Z//2)
else:
  print(Z*Z//2+1)