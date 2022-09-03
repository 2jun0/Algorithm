import sys
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

def has_num(arr, num):
  start = 0
  end = len(arr) - 1
  while start < end:
    mid = (start + end) // 2
    if num <= arr[mid]:
      end = mid
    else:
      start = mid + 1
  return arr[start] == num

An, Bn = input_n(int) # 무시
A = input_n(int)
B = input_n(int)

A.sort()
B.sort()

no_sub_nums = []
for a in A:
  if not has_num(B, a):
    no_sub_nums.append(a)

print(len(no_sub_nums))
if no_sub_nums:
  print(' '.join(list(map(str, no_sub_nums))))