import sys

def input(_type=str):
	return _type(sys.stdin.readline().rstrip())
def input_n(_type):
	return list(map(_type, input().split()))

input()
S = input()
M = 1234567891
r = 31

def hash(s):
  sum = 0
  for i, c in enumerate(s):
    a = ord(c)-ord('a')+1
    sum = (sum + (a*(r**i)%M)%M)%M

  return sum
print(hash(S))