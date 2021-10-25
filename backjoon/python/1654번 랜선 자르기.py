import sys

def input(_type=str):
	return _type(sys.stdin.readline().rstrip())
def input_n(_type):
	return list(map(_type, input().split()))

K, N = input_n(int)
A = [input(int) for _ in range(K)]

def p(x):
  """랜선 x cm를 N개 이상 만들 수 있는지의 여부"""
  cnt = 0
  for a in A:
    cnt += a//x

  return True if cnt >= N else False

first, end = (0, 2**31)
while first < end:
  mid = (first + end) // 2
  p_mid = p(mid)

  if p_mid:
    # mid가 괜찮으면 더 크게
    first = mid+1
  else:
    # 아니라면 더 작게
    end = mid
print(first-1)