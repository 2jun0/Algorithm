import sys

def input(_type=str):
	return _type(sys.stdin.readline().rstrip())
def input_n(_type):
	return list(map(_type, input().split()))

N, M = input_n(int)
A = input_n(int)

def p(x):
  """x높이로 자르면 적어도 M미터의 나무를 얻을 수 있는가?"""
  cnt = 0
  for a in A:
    if x < a:
      cnt += a-x
  if cnt >= M:
    return True
  else:
    return False

first, end = (0, 1000000000)
while first < end:
  mid = (first + end)//2
  p_mid = p(mid)
  
  if p_mid:
    first = mid+1
  else:
    end = mid

print(first-1)