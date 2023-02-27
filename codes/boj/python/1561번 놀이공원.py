import sys
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

'''
O(n) = logn
Max O(n) = 10,000*log(2,000,000,000*30) = 360,000
'''

def get_used_cnt(time):
  '''time시간이 주어졌을 때, 최대 이용 어린이 수 구하기'''
  used_cnt = 0
  for during in durings:
    used_cnt += time // during + 1
  
  return used_cnt

def get_last_used_ride_idx(time, used_cnt):
  '''time시간과 used_cnt 이용 어린이 수가 주어졌을 때, 마지막으로 타게되는 놀이기구 번호 구하기
  - 이용된 놀이기구 중, 남은 이용시간(time % during)이 가장 짧은->idx이 큰-> 순으로 정렬해서 초과된 수(used_cnt - N) 번째를 찾음
  '''
  # 남은 이용시간, idx
  candidiates = []

  for idx, during in enumerate(durings):
    candidiates.append((time % during, -idx))
  
  candidiates.sort()

  return -candidiates[used_cnt-N][1]

def find_last_used_ride_idx():
  '''마지막에 타는 놀이기구 번호 찾기'''
  start = 0
  end = N * max(durings)

  while start < end:
    mid = (start + end) // 2
    if get_used_cnt(mid) >= N:
      end = mid
    else:
      start = mid + 1
  
  # lower bound가 없는 경우
  if get_used_cnt(end) < N:
    end += 1
    
  return get_last_used_ride_idx(end, get_used_cnt(end))

N, M = input_n(int)
durings = input_n(int)

print(find_last_used_ride_idx() + 1)