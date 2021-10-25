import sys
sys.setrecursionlimit(10000000) # 재귀 제한 풀기

def _input(_type=str):
	return _type(sys.stdin.readline().rstrip())
def _input_n(_type):
	return list(map(_type, _input().split()))


N = _input(int)
G = [_input_n(int) for _ in range(N)]

for m in range(N):
  for s in range(N):
    for e in range(N):
      if G[s][m] * G[m][e] == 1:
        G[s][e] = 1

for i in range(N):
  if i != 0: print()
  for j in range(N):
    if j != 0: print(' {}'.format(G[i][j]), end='')
    else: print(G[i][j], end='')
        
