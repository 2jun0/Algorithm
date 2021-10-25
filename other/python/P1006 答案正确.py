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

N = input(int)
for _ in range(N):
  B,C = -1,-1
  s = input()
  ok = True
  for i, c in enumerate(s):
    if c == 'B': 
      if B!=-1: 
        ok=False
        break
      B = i
    elif c == 'C': 
      if C!=-1: 
        ok=False
        break
      C= i
    elif c != 'D':
      ok=False
      break

  if B==-1 or C==-1 or B>C:
    ok=False

  if ok:
    cf, cm, cb = B, C-B-1, len(s)-C-1
    if cb < 0 or cf < 0 or cm < 1 or cf*cm != cb:
      ok = False

  if ok:
    print('YES')
  else:
    print('NO')