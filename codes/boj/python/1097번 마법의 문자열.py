import sys
from itertools import permutations

def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

def get_p(s):
  p = [0]*len(s)
  l = 0
  for r in range(1, len(s)):
    while l > 0 and s[r] != s[l]:
      l = p[l-1]
    if s[r] == s[l]:
      l += 1
      p[r] = l
  return p

def kmp(s, m, p):
  cnts = [0]*len(s)
  l = 0
  for _ in range(2):
    for r, c in enumerate(s):
      while l > 0 and c != m[l]:
        l = p[l-1]
      if c == m[l]:
        l += 1
        cnts[r] = l
        if l == len(p):
          l = p[l-1]
  
  return cnts

def get_T(s):
  p = get_p(s)
  return kmp(s, s, p).count(len(s))

N = input(int)
S = [input() for _ in range(N)]
K = input(int)
cnt = 0

for words in permutations(S):
  s = ''.join(words)
  T = get_T(s)
  
  if K == T:
    cnt += 1
    
print(cnt)
  