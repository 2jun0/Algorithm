import sys
sys.setrecursionlimit(10000000) # 재귀 제한 풀기
INF = 10**8
def input(_type=str):
	return _type(sys.stdin.readline()[:-1])
def input_n(_type=str):
	return list(map(_type, input().split()))
def print_n(L, join_str=' '):
  s = ''
  for l in L[:-1]: s+='{}{}'.format(l, join_str)
  s+='{}'.format(L[-1])
  print(s)

S = input()
s1 = []
s2 = []
i = 0
while i < len(S):
  if S[i] == '(':
    s1.append(S[i])
  elif S[i] == ')':
    while s1[-1] != '(':
      s2.append(s1.pop())
    s1.pop()
  elif S[i] in ['*', '/']:
    while len(s1) > 0 and s1[-1] in ['*', '/']:
      s2.append(s1.pop())
    s1.append(S[i])
  elif S[i] in ['+', '-']:
    while len(s1) > 0 and s1[-1] in ['*', '/', '+', '-']:
      s2.append(s1.pop())
    s1.append(S[i])
  else:
    s2.append(S[i])
  i+=1

while len(s1) > 0:
  s2.append(s1.pop())
print_n(s2,'')