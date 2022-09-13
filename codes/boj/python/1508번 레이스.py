import sys
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

# referee : 심판

'''
주의 요망
dfs vs 이분탐색

dfs : 2**50
이분탐색 : 50*log1,000,000 = 5,000

이분탐색 승!
'''
INF = 10**10

def get_referee_cnt_and_bitmask(min_dist):
  '''최소 거리 min_dist일때 가능한 최대 심판 수 & bitmask 구하기
  - min_dist가 0이면 무한 루프에 빠짐
  '''
  assert min_dist > 0

  cnt = 1
  # bitmask는 사전순 맨 뒤가 답이므로, 가장 빠른 방법을 찾는게 맞다.
  bitmask = '1'
  # start point를 처음으로 고정하는 것이 가장 최선의 방법이다.
  last_pos = pos[0]
    
  for idx in range(1,K):
    # 개수가 M보다 크면 안된다. (bitmask 때문임)
    if pos[idx] - last_pos >= min_dist and cnt < M:
      cnt += 1
      bitmask += '1'
      last_pos = pos[idx]
    else:
      bitmask += '0'

  return cnt, bitmask

def find_bitmask():
  '''비트마스크(정답) 찾기'''
  start = 1
  end = N

  while start < end:
    mid = (start + end) // 2
    cnt, _ = get_referee_cnt_and_bitmask(mid)
    if cnt < M:
      end = mid
    else:
      start = mid + 1

  # 예외상황 처리 -> upper bound값이 범위안에 있는 경우
  end_cnt, end_bitmask = get_referee_cnt_and_bitmask(end)
  if end_cnt == M:
    return end_bitmask

  _, bitmask = get_referee_cnt_and_bitmask(end-1)
  return bitmask

N, M, K = input_n(int)
pos = input_n(int)

print(find_bitmask())