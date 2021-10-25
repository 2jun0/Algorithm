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

d = input(int)
m = input(int)
n = input(int)
G = input_n(int)
G.sort()

t1, t2= [], [m]

for g in G:
  t1 = t2
  t2 = [-1]*(len(t1)+1)
  for i, t in enumerate(t1):
    if t1[i] >= g:
      t2[i] = max(t2[i], t1[i])
      t2[i+1] = max(t2[i+1], g+m)
result = -1
for i, t in enumerate(t2):
  if d<=t:
    result = i
    break
print(result)