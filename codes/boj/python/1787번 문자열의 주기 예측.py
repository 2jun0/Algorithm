import sys

def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

def get_fail(s):
  fail = [0]*len(s)
  l = 0
  for r in range(1, len(s)):
    while l > 0 and s[l] != s[r]:
      l = fail[l-1]
    if s[l] == s[r]:
      l += 1
      fail[r] = l
  return fail

def get_p(fail):
  p = [0]*len(fail)
  for i in range(len(p)): 
    l = fail[i]
    
    if l == 0:
      continue
    
    if l > 0 and fail[l-1] > 0:
      l = fail[l-1]
      p[i] = p[l-1] - (l-1) + i
    else:
      p[i] = i + 1 - l
  
  return p
  
n = input(int)
S = input()
fail = get_fail(S)
  
print(sum(get_p(fail)))