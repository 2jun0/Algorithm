from collections import deque
import sys
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

# O(n) = n*n (1,000,000)
def check_sqaure(length):
  for sy in range(N-length):
    for sx in range(N-length):
      if not is_top_left[sy][sx]:
        continue

      nums = set()
      flag = True
      for y in range(sy, sy+length):
        for x in range(sx, sx+length):
          if table[y][x] == 0 or (table[y][x] not in nums and len(nums) == 2):
            flag = False
            break

          nums.add(table[y][x])

        if not flag:
          break
      
      if flag:
        return True
  
  return False

# O(n) = logn (10)
def get_max_sqaure_size():
  # binary search
  # upper bound
  s_len = 1
  e_len = N

  while s_len < e_len:
    mid_len = (s_len + e_len) // 2

    if not check_sqaure(mid_len):
      e_len = mid_len
    else:
      s_len = mid_len+1

  if e_len == N:
    return e_len**2
  else:
    return (e_len - 1)**2

N, M = input_n(int)
table = [[0]*N for _ in range(N)]
is_top_left = [[True]*N for _ in range(N)]

for _ in range(M):
  X, Y, L, F = input_n(int)
  for y in range(Y, Y+L):
    for x in range(X, X+L):
      table[y][x] = F

for y in range(1,N):
  for x in range(1,N):
    if table[y][x] == 0:
      is_top_left[y][x] = False
      continue

    if [table[y-1][x-1], table[y-1][x], table[y][x-1]].count(table[y][x]) != 3:
      is_top_left[y][x] = True
      

print(get_max_sqaure_size())