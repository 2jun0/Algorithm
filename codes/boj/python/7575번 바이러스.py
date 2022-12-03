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

def kmp(s, m, p):
  l = 0
  for c in s:
    while l > 0 and m[l] != c:
      l = p[l-1]
    if m[l] == c:
      l+=1
      if l == len(p):
        return True
  return False

N, K = input_n(int)
programs = []
for _ in range(N):
  M = input(int)
  programs.append(input_n(int))

found = False
for code_idx in range(0, len(programs[0])-K+1):
  codes = programs[0][code_idx:code_idx+K]
  reversed_codes = codes[::-1]
  
  p = get_p(codes)
  reversed_p = get_p(reversed_codes)
  
  every_find = True
  for o_idx in range(1, N):
    if not kmp(programs[o_idx], codes, p) and not kmp(programs[o_idx], reversed_codes, reversed_p):
      every_find = False
      break
  
  if every_find:
    found = True
    break
  
if found:
  print('YES')
else:
  print('NO')