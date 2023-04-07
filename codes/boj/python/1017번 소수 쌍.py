import sys

def input(type_=str):
	return type_(sys.stdin.readline().rstrip())
def input_n(type_):
	return list(map(type_, input().split()))

def init_prime(is_prime, m):
  is_prime[0] = False
  is_prime[1] = False
  
  for x in range(m+1):
    if is_prime[x]:
      for nx in range(x+x, m+1, x):
        is_prime[nx] = False

def dfs(i, adjs, visited, connect):
  if i == N:
    return True
  
  if visited[i]: return False
  visited[i] = True
  
  for ni in adjs[i]:
    if connect[ni] == -1 or dfs(connect[ni], adjs, visited, connect):
      connect[ni] = i
      return True
    
  return False

N = input(int)
A = input_n(int)

is_prime = [True]*2001
init_prime(is_prime, 2000)

adjs = [[] for _ in range(N)]
for xi, x in enumerate(A):
  for ni, nx in enumerate(A):
    if xi == ni:
      continue
    
    if is_prime[x + nx]:
      adjs[xi].append(ni)

# 0과 누구를 매치할까?
ans = []
for ni in adjs[0]:
  connect = [-1]*N
  cnt = 2
  connect[0] = ni
  connect[ni] = 0
  for i in range(1, N):
    if i == ni:
      continue
    
    visited = [False]*N
    visited[0] = True
    visited[ni] = True
    if dfs(i, adjs, visited, connect):
      cnt += 1

  if cnt == N:
    ans.append(A[ni])
  
if not ans:
  ans = [-1]
  
ans.sort()
print(' '.join(map(str, ans)))