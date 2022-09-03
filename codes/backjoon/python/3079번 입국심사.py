import sys
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

def get_frends_cnt(time):
  cnt = 0
  for t in T:
    cnt += time // t
  return cnt

def find_min_time(M):
  start = 0
  end = 10**18 # 엄청 크지만.. 이게 맞다. M의 최댓값 * T의 최댓값
  while start < end:
    mid = (start + end) // 2
    if M <= get_frends_cnt(mid):
      end = mid
    else:
      start = mid + 1

  return end

N, M = input_n(int)
T = [input(int) for _ in range(N)]

print(find_min_time(M))