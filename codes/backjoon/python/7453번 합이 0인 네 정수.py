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

n = input(int)
table = [input_n(int) for _ in range(n)]
A = [t[0] for t in table]
B = [t[1] for t in table]
C = [t[2] for t in table]
D = [t[3] for t in table]

CD = {}
for c in C:
  for d in D:
    cd=c+d
    try: CD[cd]+=1
    except: CD[cd] = 1

cnt = 0
for a in A: 
  for b in B:
    ab=a+b
    try: cnt += CD[-ab]
    except: pass
print(cnt)