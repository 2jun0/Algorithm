import sys
sys.setrecursionlimit(10000000) # 재귀 제한 풀기

def _input(_type=str):
	return _type(sys.stdin.readline().rstrip())
def _input_n(_type):
	return list(map(_type, _input().split()))

def get_2017_rewards(num):
  if num == 0: return 0
  if num == 1:
    return 5000000
  if num <= 3:
    return 3000000
  if num <= 6:
    return 2000000
  if num <= 10:
    return 500000
  if num <= 15:
    return 300000
  if num <= 21:
    return 100000
  return 0

def get_2018_rewards(num):
  if num == 0: return 0
  if num == 1:
    return 5120000
  if num <= 3:
    return 2560000
  if num <= 7:
    return 1280000
  if num <= 15:
    return 640000
  if num <= 31:
    return 320000
  return 0

T = _input(int)
for _ in range(T):
  a, b = _input_n(int)
  print(get_2017_rewards(a) + get_2018_rewards(b))

