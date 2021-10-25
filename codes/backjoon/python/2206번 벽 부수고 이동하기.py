import sys
sys.setrecursionlimit(10000000) # 재귀 제한 풀기
INF = 10**8
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))
def print_n(L, join_str=' '):
  s = ''
  for l in L[:-1]: s+='{}{}'.format(l, join_str)
  s+='{}'.format(L[-1])
  print(s)

N, M = input_n(int)
table = []
for _ in range(N):
  L = []
  for c in input(): L.append(int(c))
  table.append(L)

visited = [[[False, False] for _ in range(M)] for _ in range(N)]
dist = [[[INF, INF] for _ in range(M)] for _ in range(N)]

def conflict(i,j,d,b):
  if not (0<=i<N and 0<=j<M): return True
  if dist[i][j][b] <= d or visited[i][j][b]: return True
  if b==1 and table[i][j]==1: return True
  return False

# i, j, d, break?
s1 = []
s2 = [(0,0,0)]
d = 1
while len(s2) > 0:
  s2, s1 = s1, s2
  while len(s1) > 0:
    i, j, b = s1.pop()
    if conflict(i,j,d,b): continue
    if b == 0 and table[i][j] == 1: b = 1
    visited[i][j][b] = True
    dist[i][j][b] = d
    T = [(i-1,j,b),(i+1,j,b),(i,j-1,b),(i,j+1,b)]
    s2.extend(T)
  d+=1
result = min(dist[-1][-1][0], dist[-1][-1][1])
print(result if result < INF else -1)