import sys
sys.setrecursionlimit(10000000) # 재귀 제한 풀기
INF = 10**8
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))
def print_n(L, join_str=' '):
  for i,l in enumerate(L): print(l, end=join_str if i<len(L)-1 else '\n')

N, M = input_n(int)
table = [input_n(int) for _ in range(N)]
for i in range(N):
  for j in range(N):
    if i>0 and j>0: table[i][j]-=table[i-1][j-1]
    if i+1 < N: table[i+1][j] += table[i][j]
    if j+1 < N: table[i][j+1] += table[i][j]
    

for _ in range(M):
  x1, y1, x2, y2 = input_n(int)
  x1, y1, x2, y2 = x1-1, y1-1, x2-1, y2-1
  result = table[x2][y2]
  if y1>0: result-=table[x2][y1-1]
  if x1>0: result-=table[x1-1][y2]
  if y1>0 and x1>0: result+=table[x1-1][y1-1]
  print(result)