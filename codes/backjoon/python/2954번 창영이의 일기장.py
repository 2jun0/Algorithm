import sys
sys.setrecursionlimit(10000000) # 재귀 제한 풀기
INF = 10**10
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))
def print_n(L, join_str=' '):
  for i,l in enumerate(L): print(l, end=join_str if i<len(L)-1 else '\n')
def LL(n,m,d=0): return [[d]*n for _ in range(m)]

L = input()
S = ''
flag_aeiou = False
flag_aeiouP = False
for l in L:
  if flag_aeiou:
    flag_aeiou = False
    flag_aeiouP = True
    continue
  if flag_aeiouP:
    flag_aeiouP = False
    continue

  if l in ['a','e','i','o','u']:
    flag_aeiou = True

  S+=l
print(S)