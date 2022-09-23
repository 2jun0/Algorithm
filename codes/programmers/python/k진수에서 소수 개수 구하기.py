
def is_prime(x):
  '''소수 판별 함수 (최대 O(n) = 1,000,000'''
  if x == 1:
    return False

  for i in range(2, min(x, int(x**.5)+1)):
    if x % i == 0:
      return False
  return True

def get_n_k_str(n, k):
  k_str = '' # n을 k진수로 바꾼 값 (문자열)

  while n > 0:
    k_str = str(n % k) + k_str
    n //= k
  
  return k_str

def solution(n, k):
  k_str = get_n_k_str(n, k)

  prime_cnt = 0
  buf = ''
  for c in k_str:
    if c == '0':
      if buf and is_prime(int(buf)):
        prime_cnt += 1
      buf = ''
    else:
      buf+=c

  if buf:
    if is_prime(int(buf)):
      prime_cnt += 1

  return prime_cnt

