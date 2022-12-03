import sys

def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

def get_pattern(s):
  p = [0]*len(s)
  left = 0
  
  for right in range(1, len(s)):
    while left > 0 and s[left] != s[right]: 
      left = p[left-1]
    
    if s[left] == s[right]:
      left += 1
      p[right] = left

  return p

while True:
  s = input()
  
  if s == '.':
    break
  
  p = get_pattern(s)
  a = len(s) - p[-1]
  
  if len(s) % a == 0:
    print(len(s)//a)
  else:
    print(1)