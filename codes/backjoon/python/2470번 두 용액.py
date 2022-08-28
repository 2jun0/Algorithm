import sys
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

INF = 10**10

min_abs_sum = INF
min_nums = None

def find_min_sum(A, idx):
  global min_abs_sum, min_nums

  start = idx+1
  end = len(A)-1

  # A[start]+x <= A[mid]+x <= A[end]+x
  while start < end:
    mid = (start + end) // 2
    if A[mid] + A[idx] > 0: # 0 <= A[end]+x
      end = mid
    else: # A[start]+x <= 0 < A[mid]+x
      start = mid+1

  find_idxs = [end]
  if end != len(A)-1 and end-1 != idx:
    find_idxs.append(end-1)

  for find_idx in find_idxs:
    abs_sum = abs(A[idx] + A[find_idx])
    if min_abs_sum > abs_sum:
      min_abs_sum = abs_sum
      min_nums = [A[idx], A[find_idx]]

N = input(int)
A = input_n(int)
A.sort()

for idx in range(N-1):
  find_min_sum(A, idx)

print(min_nums[0], min_nums[1])