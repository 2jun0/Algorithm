import sys

INF = 10**8
def input(_type=str):
	return _type(sys.stdin.readline().rstrip())
def input_n(_type=str):
	return list(map(_type, input().split()))
def print_n(L):
  s = ''
  for l in L: s+='{} '.format(l)
  print(s[:-1])

M, N, H = input_n(int)
A = [[input_n(int) for _ in range(N)] for _ in range(H)]

s = []
s2 = []
for k, _A in enumerate(A):
  for i, __A in enumerate(_A):
    for j, a in enumerate(__A):
      if a==1: 
        s2.append((k,i,j))

def ok(k,i,j):
  return (0<=k<H and 0<=i<N and 0<=j<M) and A[k][i][j]==0

day = -1
while len(s2) > 0:
  day+=1
  s, s2 = s2, s
  while len(s) > 0:
    k,i,j = s.pop()
    t = [(k-1,i,j), (k,i-1,j),(k,i+1,j),(k,i,j-1),(k,i,j+1), (k+1,i,j)]
    for tk, ti, tj in t:
      if ok(tk,ti,tj):
        s2.append((tk,ti,tj))
        A[tk][ti][tj] = 1

flag = True
for k, _A in enumerate(A):
  for i, __A in enumerate(_A):
    for j, a in enumerate(__A):
      if a==0:
        flag = False
        break
    if not flag: break
  if not flag: break

if flag: print(day)
else: print(-1)