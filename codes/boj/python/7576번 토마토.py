import sys

INF = 10**8
def input(_type=str):
	return _type(sys.stdin.readline().rstrip())
def input_n(_type):
	return list(map(_type, input().split()))

M, N = input_n(int)
A = [input_n(int) for _ in range(N)]

s = []
s2 = []
for i, _A in enumerate(A):
  for j, a in enumerate(_A):
    if a==1: 
      s2.append((i,j))

def ok(i,j):
  return (0<=i<N and 0<=j<M) and A[i][j]==0

day = -1
while len(s2) > 0:
  day+=1
  s, s2 = s2, s
  while len(s) > 0:
    i,j = s.pop()
    t = [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]
    for ti, tj in t:
      if ok(ti,tj):
        s2.append((ti,tj))
        A[ti][tj] = 1

flag = True
for i, _A in enumerate(A):
  for j, a in enumerate(_A):
    if a==0:
      flag = False
      break
  if not flag: break

if flag: print(day)
else: print(-1)