import sys
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

def get_primes(limit):
  is_prime = [True] * (limit+1)
  is_prime[0] = False
  is_prime[1] = False
  primes = []
  for x in range(2, limit+1):
    if is_prime[x]:
      primes.append(x)
      for y in range(x+x, limit+1, x):
        is_prime[y] = False
  return is_prime, primes

is_prime, primes = get_primes(1000000)

while True:
  n = input(int)
  if n == 0:
    break

  for prime in primes:
    if n-prime > 0 and is_prime[n-prime]:
      print(f'{n} = {prime} + {n-prime}')
      break
  else:
    print('Goldbach\'s conjecture is wrong.')