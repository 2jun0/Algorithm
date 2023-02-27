import sys

def input(type=str):
  return type(sys.stdin.readline().strip())
def input_n(type=str):
  return list(map(type, input().split()))

def ask(k, i):
  print(f'? {k} {i}')
  sys.stdout.flush()
  return input(int)

def answer(A):
  print('!', *A)
  sys.stdout.flush()

M, N, Q = input_n(int)
maxA = input_n(int)
checksByIdx = [[False] + [True]*a for a in maxA]

for idx in range(1, M+1):
  a = ask(idx, idx)
  checksByIdx[idx-1][a] = False

A = []
for checks in checksByIdx:
  for num, check in enumerate(checks):
    if check:
      A.append(num)
      break

answer(A)