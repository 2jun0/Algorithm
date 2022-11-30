import sys
import re

def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

cmds = input()
if re.search(r'(^[+-/*])|([+-/*(][+-/*][\d])|([)][\d])|([\d][(])|(\(\))', cmds):
  print('ROCK')
else:
  try:
    print(eval(cmds.replace('/', '//')))
  except:
    print('ROCK')