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
match = True

flag_start = True
flag_1 = False
flag_10 = False
flag_100 = False
flag_100_ = False
flag_1001 = False
flag_1001_ = False
flag_0 = False
flag_01 = False
next_flag_start = False
next_flag_1 = False
next_flag_10 = False
next_flag_100 = False
next_flag_100_ = False
next_flag_1001 = False
next_flag_1001_ = False
next_flag_0 = False
next_flag_01 = False
for c in L:
  if flag_start:
    next_flag_start = False
    if c == '1': next_flag_1 = True
    if c == '0': next_flag_0 = True
  if flag_1:
    next_flag_1 = False
    if c == '0': next_flag_10 = True
  if flag_10:
    next_flag_10 = False
    if c == '0': next_flag_100 = True
  if flag_100:
    next_flag_100 = False
    if c == '0': next_flag_100_ = True
    if c == '1': next_flag_1001 = True
  if flag_100_:
    next_flag_100_ = False
    if c == '0': next_flag_100_ = True
    if c == '1': next_flag_1001 = True
  if flag_1001:
    next_flag_1001 = False
    if c == '0': next_flag_0 = True
    if c == '1': 
      next_flag_1001_ = True
      next_flag_1 = True
  if flag_1001_:
    next_flag_1001_ = False
    if c == '0': next_flag_0 = True
    if c == '1': 
      next_flag_1001_ = True
      next_flag_1 = True
  if flag_0:
    next_flag_0 = False
    if c == '1': next_flag_01 = True
  if flag_01:
    next_flag_01 = False
    if c == '0': next_flag_0 = True
    if c == '1': next_flag_1 = True

  flag_start = next_flag_start
  flag_1 = next_flag_1
  flag_10 = next_flag_10
  flag_100 = next_flag_100
  flag_100_ = next_flag_100_
  flag_1001 = next_flag_1001
  flag_1001_ = next_flag_1001_
  flag_0 = next_flag_0
  flag_01 = next_flag_01

  if not(flag_start|flag_1|flag_10|flag_100|flag_100_|flag_1001|flag_1001_|flag_0|flag_01):
    match = False
    break
match = match&(flag_1001|flag_1001_|flag_01)

print('SUBMARINE' if match else 'NOISE')
  