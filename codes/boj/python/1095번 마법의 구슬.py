import sys

def input(type_=str):
	return type_(sys.stdin.readline().rstrip())
def input_n(type_):
	return list(map(type_, input().split()))

# thanks to johnny8337
def init_is_prime(is_prime, m):
  is_prime[0] = False
  is_prime[1] = False
  
  for p in range(2, m+1):
    if is_prime[p]:
      for notp in range(p+p, m+1, p):
        is_prime[notp] = False

def pcnt(n, prime):
  '''n!에서 prime의 개수 구하기'''
  x = prime
  cnt = 0
  while x <= n:
    cnt += n // x
    x *= prime
  
  return cnt

def factorize(n, is_prime, m):
  '''소인수 분해'''
  factors = {}
  for p in range(2, int(n**0.5)+1):
    if not is_prime[p]:
      continue
    
    while n % p == 0:
      factors[p] = factors.setdefault(p, 0) + 1
      n //= p
  if n != 1:
    factors[n] = 1
  return factors

def match(afactors: dict, bfactors):
  '''bfactors가 afactors으로 나누어 지는지 인지 확인'''
  for f, cnt in afactors.items():
    if f not in bfactors:
      return False
    
    if bfactors[f] < cnt:
      return False
    
  return True

def get_max_x(m, sf_factors, is_prime):
  '''답을 구하는 함수'''
  for x in range(m, -1, -1):
    factors = factorize(x, is_prime, x)
    if match(factors, sf_factors):
      return x
  return -1

S, F, M = input_n(int)
is_prime = [True]*(M+1)
init_is_prime(is_prime, M)

# S+F의 소인수 구하기
sf_factors = {}
for p in range(M+1):
  if not is_prime[p]:
    continue
  
  cnt = pcnt(S+F, p) - pcnt(S, p) - pcnt(F, p)
  
  if cnt > 0:
    sf_factors[p] = cnt

print(get_max_x(M, sf_factors, is_prime))