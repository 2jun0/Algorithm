import sys

def input(_type=str):
	return _type(sys.stdin.readline().rstrip())
def input_n(_type):
	return list(map(_type, input().split()))


N = input(int)
k = input(int)

def p(x):
  """NxN인 배열 A에서 x보다 작거나 같은 숫자 개수 구하는 함수"""
  cnt = 0

  for i in range(1, N+1):
    # i * j <= x에서, j의 개수는
    # len(J) = x//i 이다. (구구단을 생각해보자.)
    len_j = x//i
    cnt += len_j if len_j < N else N

  return cnt

def get_closest(x):
  """NxN인 배열 A에서 x보다 작거나 같은 숫자 중 가장 가까운 수 구하는 함수"""
  closest = 0
  for i in range(1, N+1):
    max_j = x//i if x//i < N else N
    closest = max(closest, max_j*i)
  return closest

def b_search(p_num, start, end):
  """binary search"""
  while start < end:
    mid = (start + end)//2
    p_mid = p(mid)

    if p_num < p_mid: # start ~ mid -1
      end = mid
    elif p_mid < p_num: # mid + 1 ~ end - 1
      start = mid+1
    else:
      return get_closest(mid)

  return get_closest(start)

print(b_search(k, 1, N*N+1))