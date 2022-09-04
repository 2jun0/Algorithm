import sys

INF = 10**8
def input(_type=str):
	return _type(sys.stdin.readline().rstrip())
def input_n(_type=str):
	return list(map(_type, input().split()))
def print_n(L):
  s = ''
  for l in L: s+='{} '.format(l)
  print(s[:-1])
N = input(int)
M = input(int)
S = input()

cnt = 0
i_flag = False
find_i_flag = False
result = 0
for s in S:
  if not find_i_flag and s=='I': find_i_flag = True
  if not find_i_flag: continue

  if s == 'I':
    if i_flag: cnt=1
    else: cnt+=1
    i_flag = True
  if s == 'O': 
    if i_flag: cnt+=1
    else: cnt=0
    i_flag = False
  if cnt//2 >= N and cnt%2==1: result+=1

print(result)
