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

N, M = input_n(int)
table = []
for _ in range(N):
  s = input()
  table.append([int(x) for x in s])

table2 = [[INF]*M for _ in range(N)]
s = [(0,0,0)]

def conflict(i,j,d):
  if (0<=i<N and 0<=j<M) and (table[i][j]==1 and table2[i][j]>d): return False
  else: return True

while len(s) > 0:
  i, j, d = s.pop()
  d+=1
  if conflict(i,j,d): continue
  table2[i][j] = d
  T = ((i-1,j),(i+1,j),(i,j-1),(i,j+1))
  for i,j in T: s.append((i,j,d))
print(table2[N-1][M-1])