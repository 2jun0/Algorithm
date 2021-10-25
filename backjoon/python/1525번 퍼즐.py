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

puzzle = [input_n(int) for _ in range(3)]
# find zero and puzzle to str
zero_pos = None
tmp = ''
for i in range(3):
  for j in range(3):
    tmp+=str(puzzle[i][j])
    if puzzle[i][j] == 0:
      zero_pos = (i,j)

puzzle = tmp+' '
visited = set([puzzle])

s1 = []
s2 = [(zero_pos[0], zero_pos[1], puzzle)]
result = -1
cnt = 0
while len(s2) > 0:
  s1, s2 = s2, s1
  while len(s1) > 0:
    y,x,puzzle = s1.pop()

    if puzzle == '123456780 ':
      s1 = []
      s2 = []
      result = cnt
      break

    idx = y*3 + x
    for ty, tx in getLRUD(y,x):
      if 0<=ty<3 and 0<=tx<3:
        tidx = ty*3 + tx
        minidx, maxidx = min(tidx, idx), max(tidx, idx)
        tpuzzle = puzzle[:minidx] + puzzle[maxidx] + puzzle[minidx+1:maxidx] + puzzle[minidx] + puzzle[maxidx+1:]

        if tpuzzle in visited: continue

        visited.add(tpuzzle)

        s2.append((ty, tx, tpuzzle))
  cnt+=1
print(result)
