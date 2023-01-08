import sys

def input(_type=str):
  return _type(sys.stdin.readline().strip())
def input_n(_type=str):
  return list(map(_type, input().split()))

p = 998244353

def factorial(x):
  s = 1
  for i in range(2, x+1):
    s = multi(s, i)
  return s

def pow(x, a):
  if a == 0:
    return 1
  if a == 1:
    return x
  
  tmp = pow(x, a//2)
  s = multi(tmp, tmp)
  if a % 2 != 0:
    s = multi(s, x)
  
  return s

def mod_inv(x):
  return pow(x, p-2)

def combination(n, m):
  if n < m:
    return 0
  
  return multi(factorial(n), mod_inv(factorial(m)), mod_inv(factorial(n-m)))

def multi(*a):
  s = 1
  for x in a:
    s = (s * x) % p
  return s

k = input(int)
A = input_n(int)
R = input_n(int)
x = 0

for ai in range(1, len(A)):
  if A[ai] < A[0]:
    x+=1

ans = 0
for i in range(1,k+1):
  ans += multi(combination(x, pow(2, i) - 1), factorial(pow(2, i) - 1), factorial(pow(2, k) - pow(2, i)), R[i-1])
  
print(multi(ans, mod_inv(factorial(pow(2, k) - 1))))