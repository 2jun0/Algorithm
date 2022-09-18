import sys
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

def get_group_cnts(max_sum):
  '''최대 그룹의 합(max_sum)으로 최소 그룹 별 숫자 개수를 구한다'''
  
  group_sum = nums[0]
  group_cnts = [1]
  for idx in range(1,N):
    if N-idx == M-len(group_cnts) or group_sum + nums[idx] > max_sum:
      group_sum = 0
      group_cnts.append(0)

    group_cnts[-1] += 1
    group_sum += nums[idx]

  return group_cnts

def find_min_max_sum_and_group_cnts():
  '''M개의 그룹 으로 나뉘어 지는 경우의 수 중 최댓값이 최소가 되는 것을 반환'''
  
  start = 1
  end = sum(nums)

  while start < end:
    mid = (start + end) // 2

    if M >= len(get_group_cnts(mid)):
      end = mid
    else:
      start = mid + 1

  return max(end, *nums), get_group_cnts(end)

N, M = input_n(int)
nums = input_n(int)

min_sum, group_cnts = find_min_max_sum_and_group_cnts()
print(min_sum)
print(*group_cnts)
