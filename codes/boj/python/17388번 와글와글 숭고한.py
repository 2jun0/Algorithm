import sys

def input(type=str):
  return type(sys.stdin.readline().strip())
def input_n(type=str):
  return list(map(type, input().split()))

S, K, H = input_n(int)
if S+K+H >= 100:
  print('OK')
else:
  L = [(S, 'Soongsil'), (K, 'Korea'), (H, 'Hanyang')]
  L.sort()
  print(L[0][1])