import sys

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

def kmp(s, match, p):
  pl = 0
  cnts = [0]*len(s)
  for _ in range(2):
    for r, c in enumerate(s):
      while pl > 0 and match[pl] != c:
        pl = p[pl-1]
      if match[pl] == c:
        pl += 1
        cnts[r] = max(cnts[r], pl)
      if pl == len(p):
        pl = p[pl-1]
  return cnts

A = input()
B = input()
p = get_p(B)

cnts = kmp(A, B, p)
print(cnts.count(len(B)))