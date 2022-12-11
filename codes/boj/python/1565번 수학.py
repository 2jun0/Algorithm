import sys
from math import gcd

def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

def multiply(*A):
  result = 1
  for a in A:
    result *= a
  return result

def lcm(*A):
  lcm_v = 1
  for a in A:
    lcm_v = lcm_v * a // gcd(lcm_v, a)
  
  return lcm_v

_ = input()
D = input_n(int)
M = input_n(int)

lcm_v = lcm(*D)
gcd_v = gcd(*M)

cnt = 0
for v in range(1, int(gcd_v**0.5)+1):
  if gcd_v % v == 0:
    if v % lcm_v == 0:
      cnt += 1
    if v!=gcd_v // v and (gcd_v // v) % lcm_v == 0:
      cnt += 1

print(cnt)