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

N, K = input_n(str)
K = int(K)
s2 = set([N])
s1 = set()
k = 0
while len(s2) > 0 and k < K:
  s1 = s2
  s2 = set()
  for L in s1:
    for i in range(len(L)):
      for j in range(i+1, len(L)):
        new_L = L[:i] + L[j] + L[i+1:j] + L[i] + L[j+1:]

        if new_L[0] != '0':
          s2.add(new_L)
  k+=1

max_v = -1
for L in s2:
  max_v = max(max_v, int(L))
print(max_v)
  
