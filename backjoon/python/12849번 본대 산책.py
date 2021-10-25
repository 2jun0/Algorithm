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

graph = [
  [1,2],
  [0,2,3],
  [0,1,3,4],
  [1,2,4,5],
  [2,3,5,6],
  [3,4,7],
  [4,7],
  [5,6]]

D = input(int)
cnts = [[0]*8 for _ in range(D+1)]
cnts[0][0] = 1

for d in range(D):
  for i in range(8):
    for j in graph[i]:
      cnts[d+1][j] = (cnts[d+1][j] + cnts[d][i]) % 1000000007
print(cnts[D][0])