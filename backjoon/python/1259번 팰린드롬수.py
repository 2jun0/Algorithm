import sys

def input(_type=str):
	return _type(sys.stdin.readline().rstrip())
def input_n(_type):
	return list(map(_type, input().split()))

s = input()
while s != '0':
  i = 0
  flag = True
  while i <= len(s)//2:
    if s[i] != s[-(i+1)]:
      flag = False
      break
    i+=1
  if flag: print('yes')
  else: print('no')

  s = input()