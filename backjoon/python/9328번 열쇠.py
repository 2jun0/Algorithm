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

T = input(int)
for _ in range(T):
  h, w = input_n(int)
  m = [input() for _ in range(h)]
  ks = input()

  key = [False]*(ord('z')-ord('a')+1)
  door = [[] for _ in range((ord('Z')-ord('A')+1))]
  visited = [[False]*w for _ in range(h)]

  if ks != '0':
    for k in ks: key[ord(k)-ord('a')] = True

  def ok(i,j):
    return 0<=i<h and 0<=j<w and m[i][j] != '*' and not visited[i][j]

  s = []
  for i in range(h):
    if m[i][0] != '*': s.append((i, 0))
    if m[i][w-1] != '*': s.append((i, w-1))
  for j in range(1,w-1):
    if m[0][j] != '*': s.append((0, j))
    if m[h-1][j] != '*': s.append((h-1, j))

  cnt = 0
  while len(s) > 0:
    i,j = s.pop()

    if not ok(i, j): continue
    if m[i][j] == '$': cnt+=1
    elif m[i][j] != '.': 
      ord_m = ord(m[i][j])
      if ord('a') <= ord_m <= ord('z'):
        key[ord_m-ord('a')] = True
        while len(door[ord_m-ord('a')]) > 0:
          di,dj = door[ord_m-ord('a')].pop()
          s.append((di,dj))

      elif ord('A') <= ord_m <= ord('Z'):
        if not key[ord_m-ord('A')]:
          door[ord_m-ord('A')].append((i, j))
          continue

    visited[i][j] = True

    for ti, tj in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
      s.append((ti,tj))
  print(cnt)