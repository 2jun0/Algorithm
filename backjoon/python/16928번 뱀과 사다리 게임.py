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

N, M = input_n(int)

DP = [INF] * 101

DP[0] = 0
DP[1] = 0
ladders = [-1] * 101
snakes = [-1] * 101

for _ in range(N):
  x, y = input_n(int)
  ladders[x] = y

for _ in range(M):
  x, y = input_n(int)
  snakes[x] = y

s = [(2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]

while len(s) > 0:
  i, dp = s.pop()
  if i >= 101: continue

  if snakes[i] != -1:
    s.append((snakes[i], dp))
    continue
  if ladders[i] != -1:
    s.append((ladders[i], dp))
    continue

  if DP[i] <= dp: continue

  DP[i] = dp

  for ti in range(i+1,i+7):
    s.append((ti, dp+1))

print(DP[100])