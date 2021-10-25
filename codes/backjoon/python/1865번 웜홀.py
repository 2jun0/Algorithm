import sys
sys.setrecursionlimit(10000000) # 재귀 제한 풀기
INF = 10**8
def input(_type=str):
	return _type(sys.stdin.readline()[:-1])
def input_n(_type=str):
	return list(map(_type, input().split()))
def print_n(L):
  s = ''
  for l in L: s+='{} '.format(l)
  print(s[:-1])

TC = input(int)
for _ in range(TC):
  N, M, W = input_n(int)
  graph=[[] for _ in range(N+1)]
  dist=[0]*(N+1)
  for __ in range(M):
    S, E, T = input_n(int)
    graph[E].append((S,T))
    graph[S].append((E,T))
  for __ in range(W):
    S, E, T = input_n(int)
    graph[S].append((E,-T))

  for __ in range(N-1):
    for S, G in enumerate(graph):
      for E, T in G:
        dist[E] = min(dist[S]+T, dist[E])
  # 음수 사이클 발견하기 (한번만 로테이션 돌리기)
  cycle = False
  for S, G in enumerate(graph):
    for E, T in G:
      if dist[E] > dist[S]+T:
        cycle=True
        break
    if cycle: break
  
  if cycle: print('YES')
  else: print('NO')