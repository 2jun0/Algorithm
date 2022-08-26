import sys
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

# 완전 탐색
#   O(N) = 2**N

# 나누기 2번만 (최적의 해가 있겠지만, N번 나누면 O(N)=2**N이 된다)
#   O(N) = O(N//2)*2 = 2**(N//2) * 2
#   O(N) = 2 ** (N//2+1)
#   O(30) = 2**(16) = 65,536

def dfs(idx, end, sum, sums):
  if sum > C:
    return

  if idx > end:
    sums.append(sum)
    return

  dfs(idx+1, end, sum, sums)
  dfs(idx+1, end, sum+A[idx], sums)

def find_upper_bound(arr, start, end, num):
  if start >= end:
    if arr[end] <= num:
      return end+1
    return end
    
  mid = (start+end)//2
  if num < arr[mid]:
    return find_upper_bound(arr, start, mid, num)
  else:
    return find_upper_bound(arr, mid+1, end, num)

N, C = input_n(int)
A = input_n(int)

start, end = 0, N-1
mid = (start+end)//2

left_sums = []
dfs(0, mid, 0, left_sums)
right_sums = []
dfs(mid+1, end, 0, right_sums)

# sort
right_sums.sort()

cnt = 0
for left_v in left_sums:
  cnt += find_upper_bound(right_sums, 0, len(right_sums)-1, C-left_v)
    
print(cnt)