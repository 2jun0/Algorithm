

import sys
sys.setrecursionlimit(100000) # 재귀 제한 풀기

def _input():
  return sys.stdin.readline().rstrip()
def _input_n(_type):
  return map(_type, _input().split())

def act():
  N = int(_input())
  S = _input()
  T = _input()
  i, j = _input_n(int)

  check_chs = [S[i], S[j]]
  check_cnt = 0

  S_i = 0
  T_i = 0
  while T_i < N and S_i < N:
    # skip check chars
    if S_i == i or S_i == j:
      S_i += 1
      continue

    if S[S_i] != T[T_i]:
      if check_cnt >= 2:
        return False

      if T[T_i] != check_chs[check_cnt]:
        return False
      S_i -= 1
      check_cnt += 1

    S_i += 1
    T_i += 1

  while T_i < N and check_cnt < 2:
    if T[T_i] != check_chs[check_cnt]:
      return False

    check_cnt += 1
    T_i += 1

  return True

if act():
  print('YES')
else:
  print('NO')
'''
[o]xoxo[x]
xox[ox]o

xoxo [ox]
xoxo xo

xoxoxxx[o]xoxo[x]
xoxoxxxxox[ox]o
'''
