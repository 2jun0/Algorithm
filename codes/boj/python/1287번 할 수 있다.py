import sys
import re

def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def run(cmd):
  s = []
  for c in cmd:
    if c in DIGITS:
      # digit
      s.append(c)
    
    elif c in ['+', '-', '/', '*', '(']:
      # expr and (
      s.append(c)
      
    elif c == ')':
      exp = ''
      while len(s) > 0 and s[-1] != '(':
        exp = s[-1]+exp
        s.pop()
        
      if len(s) == 0:
        raise SyntaxError('doesn\'t have (')
      
      s.pop()
      s.append(str(eval(exp.replace('/', '//'))))
      
  exp = ''
  while len(s) > 0:
    exp = s[-1]+exp
    s.pop()
  s.append(str(eval(exp.replace('/', '//'))))
  return int(s[-1])

cmds = input()
if re.search(r'(^[+-/*])|([+-/*(][+-/*][\d])|([)][\d])|([\d][(])|(\(\))', cmds):
  print('ROCK')
elif re.search(r'[^\d+-/*()]', cmds):
  print('ROCK')
else:
  cmds = re.sub(r'([+-/*()])0+(\d)', r'\1\2', cmds)
  cmds = re.sub(r'^0+(\d)', r'\1', cmds)
  try:
    print(run(cmds))
  except Exception as e:
    print('ROCK')