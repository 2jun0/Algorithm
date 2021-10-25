import sys
sys.setrecursionlimit(10000000) # 재귀 제한 풀기
INF = 10**10
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))
def print_n(L, join_str=' '):
  for i,l in enumerate(L): print(l, end=join_str if i<len(L)-1 else '\n')
def LL(n,m,d=0): return [[d]*n for _ in range(m)]
def avg(l): return sum(l)/len(l)

N = input(int)
graph = LL(0,N+1)
for _ in range(N-1):
  a, b = input_n(int)
  graph[a].append(b)
  graph[b].append(a)

# make sparse matrix
s = [(1, 1, b) for b in graph[1]]
SM = LL(0,N+1,1)
SM[1] = [1]
L = [-1] * (N+1)
L[1] = 0

while len(s) > 0:
  level, a, b = s.pop()
  if L[b] != -1: continue
  L[b] = level
  i = 0
  p = a
  while True:
    SM[b].append(p)
    if p==1: break

    i+=1
    if len(SM[p]) > i-1:
      p = SM[p][i-1]
    else:
      p = 1
  if len(SM[b]) == 0 or SM[b][-1] != 1:
    SM[b].append(1)

  for nxt in graph[b]:
    s.append((level+1,b,nxt))

M = input(int)
for _ in range(M):
  a,b = input_n(int)
  if L[a] > L[b]: a,b=b,a
  
  for i in range(len(SM[b])-1,-1,-1):
    if len(SM[b]) > i and L[b]-L[a] >= 2**i:
      b = SM[b][i]

  for i in range(len(SM[a])-1,-1,-1):
    if len(SM[a]) <= i or len(SM[b]) <= i: continue
    if SM[a][i] != SM[b][i]:
      a = SM[a][i]
      b = SM[b][i]
      
  if a == b:
    print(a)
  else:
    print(SM[a][0])