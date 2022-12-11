import sys

def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

def get_p(s):
  p = [0]*len(s)
  
  l = 0
  for r in range(1, len(s)):
    # find l
    while l > 0 and s[l] != s[r]:
      l = p[l-1]
    if s[l] == s[r]:
      l+=1
      p[r] = l
  
  return p

s = input()
max_p = 0
for i in range(len(s)-1):
  sub_s = s[i:]
  pattern = get_p(sub_s)
  max_p = max(max_p, *pattern)
  
print(max_p)