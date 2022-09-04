import sys
sys.setrecursionlimit(10000000) # 재귀 제한 풀기
INF = 10**8
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))
def print_n(L, join_str=' '):
  for i,l in enumerate(L): print(l, end=join_str if i<len(L)-1 else '\n')
def LL(n,m,d=0): return [[d]*n for _ in range(m)]

N = input(int)
costs = [0]*(N+1)
graph = LL(0, N+1)
c_cnt = [0]*(N+1)
s = []
for _i in range(N):
  i = _i+1
  A = input_n(int)
  costs[i] = A[0]
  c_cnt[i] = A[1]
  if c_cnt[i] > 0:
    for a in A[2:]:
      graph[a].append(i)
  else: s.append(i)

total_costs = [0]*(N+1)
for i in s: total_costs[i] = costs[i]

while len(s) > 0:
  x = s.pop()
  for y in graph[x]:
    c_cnt[y] -= 1
    total_costs[y] = max(total_costs[y], costs[y]+total_costs[x])
    if c_cnt[y] == 0: s.append(y)
print(max(total_costs)) 
      