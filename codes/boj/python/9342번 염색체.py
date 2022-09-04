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

T = input(int)
for _ in range(T):
  L = input()
  match = True

  flag_start = True
  flag_ABCDEF = False
  flag_A = False
  flag_A_ = False
  flag_AF = False
  flag_AF_ = False
  flag_AFC = False
  flag_AFC_ = False
  flag_AFCABCEDF = False

  for i, c in enumerate(L):
    next_flag_start = False
    next_flag_ABCDEF = False
    next_flag_A = False
    next_flag_A_ = False
    next_flag_AF = False
    next_flag_AF_ = False
    next_flag_AFC = False
    next_flag_AFC_ = False
    next_flag_AFCABCEDF = False

    if flag_start:
      if c in ['A','B','C','D','E','F']: next_flag_ABCDEF = True
      if c == 'A': next_flag_A = True
    if flag_ABCDEF:
      if c == 'A': next_flag_A = True
    if flag_A or flag_A_:
      if c == 'A': next_flag_A_ = True
      if c == 'F': next_flag_AF = True
    if flag_AF or flag_AF_:
      if c == 'F': next_flag_AF_ = True
      if c == 'C': next_flag_AFC = True
    if flag_AFC or flag_AFC_:
      if c == 'C': next_flag_AFC_ = True
      if c in ['A','B','C','D','E','F']: next_flag_AFCABCEDF = True

    flag_start = next_flag_start
    flag_ABCDEF = next_flag_ABCDEF
    flag_A = next_flag_A
    flag_A_ = next_flag_A_
    flag_AF = next_flag_AF
    flag_AF_ = next_flag_AF_
    flag_AFC = next_flag_AFC
    flag_AFC_ = next_flag_AFC_
    flag_AFCABCEDF = next_flag_AFCABCEDF

    if not(flag_start|flag_ABCDEF|flag_A|flag_A_|flag_AF|flag_AF_|flag_AFC|flag_AFC_|flag_AFCABCEDF):
      match = False
      break
  match = match&(flag_AFCABCEDF|flag_AFC_|flag_AFC)

  print('Infected!' if match else 'Good')
  