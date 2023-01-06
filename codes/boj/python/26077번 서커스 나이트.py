import sys
from collections import deque
def input(_type=str):
  return _type(sys.stdin.readline().strip())
def input_n(_type=str):
  return list(map(_type, input().split()))

def get_factors_by_num():
  factors_by_num = {}
  is_prime = [True]*(1_000_001)
  is_prime[0] = is_prime[1] = False
  
  for p in range(2, 1_000_001):
    if is_prime[p]:
      factors_by_num.setdefault(p, []).append(p)
      for q in range(p+p, 1_000_001, p):
        is_prime[q] = False
        factors_by_num.setdefault(q, []).append(p)
  return factors_by_num

def get_idxes_by_factor(factors_by_num, A):
  idxes_by_factor = {}
  
  for idx, a in enumerate(A):
    for factor in factors_by_num[a]:
      idxes_by_factor.setdefault(factor, []).append(idx)
      
  return idxes_by_factor

def travel(idxes_by_factor, factors_by_num, A):
  visited = [False]*N
  visited_f = set()
  
  def bfs(s):
    q = deque()
    
    visited[s] = True
    q.append(s)
    cnt = 0
    
    while q:
      idx = q.popleft()
      cnt += 1
      
      for factor in factors_by_num[A[idx]]:
        if factor in visited_f:
          continue
        
        visited_f.add(factor)
        
        for nidx in idxes_by_factor[factor]:
          if not visited[nidx]:
            visited[nidx] = True
            q.append(nidx)
            
    return cnt
  
  cnt = 0
  for idx, a in enumerate(A):
    if not visited[idx]:
      cnt = max(cnt, bfs(idx))
      
  return cnt

N = input(int)
A = input_n(int)
factors_by_num = get_factors_by_num()
idxes_by_factor = get_idxes_by_factor(factors_by_num, A)
print(travel(idxes_by_factor, factors_by_num, A))