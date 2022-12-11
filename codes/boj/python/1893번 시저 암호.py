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
      l += 1
      p[r] = l
  return p

def kmp(s, match, p):
  pl = 0
  cnts = [0]*len(s)
  for r, c in enumerate(s):
    while pl > 0 and match[pl] != c:
      pl = p[pl-1]
    if match[pl] == c:
      pl += 1
      cnts[r] = pl
    
    if pl == len(match):
      pl = p[pl-1]
    
  return cnts

def trans(s, transition):
  for i, c in enumerate(s):
    s[i] = transition[c]
  
def create_transition(A):
  transition = {}
  
  for i in range(len(A)):
    transition[A[i-1]] = A[i]
  
  return transition

T = input(int)
for _ in range(T):
  A, W, S = input(), list(map(str, input())), input()
  transition = create_transition(A)
  
  p = get_p(W)
  accpects = []
  
  for shift in range(len(A)): 
    cnts = kmp(S, W, p)
  
    if cnts.count(len(W)) == 1:
      accpects.append(shift)
      
    trans(W, transition)
      
  if len(accpects) == 0:
    print('no solution')
  elif len(accpects) == 1:
    print(f'unique: {accpects[0]}')
  else:
    print(f'ambiguous: {" ".join(map(str, accpects))}')