import sys

def input(_type=str):
	return _type(sys.stdin.readline().rstrip())
def input_n(_type):
	return list(map(_type, input().split()))

def isInt(s):
  try:
    int(s)
    return True
  except:
    return False

N, M = input_n(int)
name2num = {}
num2name = {}

for i in range(1, 1+N):
  name = input()
  name2num[name] = i
  num2name[i] = name
for _ in range(M):
  s = input()
  if isInt(s):
    s = int(s)
    print(num2name[s])
  else:
    print(name2num[s])