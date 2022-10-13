from math import gcd
from random import randint
import sys
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

# ko.wikipedia.org/wiki/밀러-라빈_소수판별법

def mabye_prime(n):
  def _mabye_prime(n, a):
    if a == n: 
      return True

    x = n-1
    while x % 2 == 0:
      if pow(a, x, n) == n-1: 
        return True
      x //= 2

    return pow(a, x, n) in [1, n-1]
    
  for a in [2,3,5,7,11,13,17,31,61,73]:
    if not _mabye_prime(n, a):
      return False
  return True

def get_factor(n, x0, c):
  def g(x):
    return (x * x + c) % n

  x, y, d = x0, x0, 1
  while d == 1:
    x = g(x)
    y = g(g(y))
    d = gcd(x - y, n)

  return d

def get_divisors(n):
  if n == 1:
    return []
  if n == 4:
    return [2,2]

  if mabye_prime(n):
    return [n]

  while True:
    x0 = randint(-n+2, n-2)
    c = randint(-100, 100)
    f = get_factor(n, x0, c)
    if f != n:
      return get_divisors(n//f) + get_divisors(f)

n = input(int)
for f in sorted(get_divisors(n)):
  print(f)