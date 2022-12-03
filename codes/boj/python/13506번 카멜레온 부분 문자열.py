import sys
from itertools import combinations

def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

def get_p(s):
  p = [0]*len(s)
  l = 0
  for r in range(1, len(s)):
    while l > 0 and s[l] != s[r]:
      l = p[l-1]
    if s[l] == s[r]:
      l+=1
      p[r] = l
  return p

def find_in_middle(s, m, p):
  pl = 0
  for r in range(1, len(s)-1):
    while pl > 0 and m[pl] != s[r]:
      pl = p[pl-1]
    if m[pl] == s[r]:
      pl += 1
      if pl == len(p):
        return True
  return False

def find_cameleon(S):
  sp = get_p(S)
  spl = sp[-1]
  while spl > 0:
    prefix = S[:spl]
    if find_in_middle(S, prefix, get_p(prefix)):
      return prefix
    spl = sp[spl-1]
  return None

S = input()
prefix = find_cameleon(S)
if prefix:
  print(prefix)
else:
  print(-1)
