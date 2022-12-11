import sys
import math
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

gcd, lcm = input_n(int)
# lcm = A * B // gcd
# lcm * gcd = A * B

AtimesB = gcd * lcm
A, B = 10**8, 10**8
for ta in range(1, int(AtimesB**.5)+1):
  if AtimesB % ta == 0:
    tb = AtimesB // ta
    if A + B > ta + tb and math.gcd(ta, tb) == gcd:
      A, B = ta, tb

print(A, B)