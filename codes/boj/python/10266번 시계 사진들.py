import sys

def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

def get_p(A):
  p = [0]*len(A)
  l = 0
  for r in range(1, len(A)):
    while l > 0 and A[l] != A[r]:
      l = p[l-1]
    if A[l] == A[r]:
      l += 1
      p[r] = l
  return p

def get_diffs(A):
  diffs = []
  for i in range(len(A)):
    diffs.append((A[i] - A[i-1]) % 360000)
  return diffs

def kmp(s, ps, p):
  pl = 0
  for _ in range(2):
    for c in s:
      while pl > 0 and c != ps[pl]:
        pl = p[pl-1]
      if c == ps[pl]:
        pl += 1
      else:
        pl = 0
    
      if pl == len(p):
        return True
  return False

N = input(int)
A = input_n(int)
B = input_n(int)

A.sort()
B.sort()

Ad = get_diffs(A)
Bd = get_diffs(B)

Bp = get_p(Bd)
 
if kmp(Ad, Bd, Bp):
  print("possible")
else:
  print("impossible")