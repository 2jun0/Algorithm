import sys
from math import gcd

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

def kmp(text, match, p):
  pl = 0
  m_cnts = [0]*len(text)
  
  for _ in range(2):
    for r, c in enumerate(text):
      while pl > 0 and match[pl] != c:
        pl = p[pl-1]
      if match[pl] == c:
        pl+=1
        m_cnts[r] = pl
        
      if pl == len(match):
        pl = p[pl-1]
  
  return m_cnts.count(len(text))

N = input(int)
text = input_n(str)
match = input_n(str)

p = get_p(match)
cnt = kmp(text, match, p)

# 분모 분자
down = N // gcd(N, cnt)
up = cnt // gcd(N, cnt)

print(f'{up}/{down}')