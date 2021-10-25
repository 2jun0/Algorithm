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
def getLRUD(i,j): return [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]

N = input(int)
A = input_n(int)

sums = {}
for i in range(N):
  for j in range(i+1, N):
    try:
      sums[A[i]+A[j]].append((i,j))
    except:
      sums[A[i]+A[j]] = [(i,j)]

cnt = 0
for k in range(N):
  try:
    flag = False
    for i,j in sums[A[k]]:
      if k != i and k != j:
        flag = True
        break
    if flag: cnt+=1
  except: pass

print(cnt)