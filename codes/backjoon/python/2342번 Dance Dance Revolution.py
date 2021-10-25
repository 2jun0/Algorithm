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

CENTER, UP, LEFT, DOWN, RIGHT = 0, 1, 2, 3, 4
F = [[1]*5 for _ in range(5)]
F[CENTER][UP], F[CENTER][LEFT], F[CENTER][DOWN], F[CENTER][RIGHT] = 2,2,2,2
F[UP][CENTER], F[UP][LEFT], F[UP][DOWN], F[UP][RIGHT] = 2,3,4,3
F[LEFT][CENTER], F[LEFT][UP], F[LEFT][DOWN], F[LEFT][RIGHT] = 2,3,3,4
F[DOWN][CENTER], F[DOWN][UP], F[DOWN][LEFT], F[DOWN][RIGHT] = 2,4,3,3
F[RIGHT][CENTER], F[RIGHT][UP], F[RIGHT][LEFT], F[RIGHT][DOWN] = 2,3,4,3

L = input_n(int)[:-1]
DP = [[[INF for _r in range(5)] for _l in range(5)] for _ in range(len(L))]
s1 = []
s2 = [
  (F[0][L[0]],L[0],0),
  (F[0][L[0]],0,L[0])
]
lv = 0
while len(s2) > 0:
  s1, s2 = s2, s1
  while len(s1) > 0:
    f, l, r = s1.pop()
    if DP[lv][l][r] <= f: continue
    DP[lv][l][r] = f
    if lv+1 >= len(L): continue 

    s2.append((f+F[l][L[lv+1]], L[lv+1], r)) # left
    s2.append((f+F[r][L[lv+1]], l, L[lv+1])) # right
  lv+=1
min_f = INF
for l_i in range(5): min_f = min(min_f, min(DP[-1][l_i]))
print(min_f)