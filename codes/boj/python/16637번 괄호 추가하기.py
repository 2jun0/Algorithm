import sys
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

def get_all_ranges(srt, end):
  '''srt부터 end까지 1, 2개 씩 묶는 모든 경우의 수를 구함'''
  if srt > end:
    return []
  if srt == end:
    return [[(srt, end)]]

  ranges = []

  for count in range(2):
    if srt+count == end:
      ranges.append([(srt,srt+count)])
    else:
      for sub_ranges in get_all_ranges(srt+count+1, end):
        ranges.append([(srt,srt+count)] + sub_ranges)
  
  return ranges

def calculate_ranges(cmds, nums, ranges):
  '''ranges[idx]씩 묶어서 계산'''

  def _calculate_range(cmds, nums, srt, end):
    '''nums기준 srt부터 end까지 계산'''

    result = nums[srt]
    for cmd_idx in range(srt, end):
      if cmds[cmd_idx] == '*':
        result *= nums[cmd_idx+1]
      elif cmds[cmd_idx] == '+':
        result += nums[cmd_idx+1]
      elif cmds[cmd_idx] == '-':
        result -= nums[cmd_idx+1]

    return result
  
  new_nums = [_calculate_range(cmds, nums, ranges[0][0], ranges[0][1])]
  new_cmds = []
  for srt, end in ranges[1:]:
    new_nums.append(_calculate_range(cmds, nums, srt, end))
    new_cmds.append(cmds[srt-1])

  return _calculate_range(new_cmds, new_nums, 0, len(new_nums)-1)

N = input(int)
cmds = []
nums = []
for i, c in enumerate(input()):
  if i%2 == 0:
    nums.append(int(c))
  else:
    cmds.append(c)

# print(get_all_ranges(0, len(nums)-1))


max_result = max(calculate_ranges(cmds, nums, ranges) for ranges in get_all_ranges(0, len(nums)-1))
print(max_result)