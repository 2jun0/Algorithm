import sys
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

def euler_phi(n):
  phi = 1
  p = 2
  while p*p <= n:
    # n 에 들어있는 소인수(prime) 개수
    prime_cnt = 0
    while n % p == 0: # gcd(n, p) != 1
      prime_cnt+=1
      n //= p

    if prime_cnt > 0:
      phi *= p**prime_cnt - p**(prime_cnt-1)

    p += 1

  if n > 1:
    phi *= n - 1
  
  return phi

n = input(int)
print(euler_phi(n))