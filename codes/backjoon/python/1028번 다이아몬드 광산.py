import sys
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

# DP 문제!

# 1 : [1,1]

# 00100 : [0,0], [0,0], [1,1], [0,0], [0,0]
# 01010 : [0,0], [1,2], [0,0], [2,1], [0,0]
# 10101 : [1,3], [0,0], [2,2], [0,0], [3,1]
# 01010 : [0,0], [2,3], [0,0], [3,2], [0,0]
# 00100 : [0,0], [0,0], [3,3], [0,0], [0,0]
# 01000 : [0,0], [1,4], [0,0], [0,0], [0,0]

# 다이아몬드 생성 조건 : 
# 왼쪽 하단 변
# 오른족 하단 변
# 왼쪽 상단 변
# 오른족 상단 변
# 을 모두 min한 것이 다이아몬드 크기임.
def get_max_size_dp():
  # dp[y][x] = [cnt up left cnt, cnt up right cnt]
  dp = [[[0,0] for _ in range(C)] for _ in range(R)]
  max_size = 0

  for y in range(R):
    for x in range(C):
      if table[y][x] == 1:
        # default
        dp[y][x] = [1,1]

        # get up left cnt
        if y-1>=0 and x-1>=0:
          dp[y][x][0] = dp[y-1][x-1][0]+1
        
        # get up right cnt
        if y-1>=0 and x+1<C:
          dp[y][x][1] = dp[y-1][x+1][1]+1

        # check if it can make diamond
        min_size_down = min(dp[y][x])

        for size in range(min_size_down, max_size, -1):
          if dp[y-(size-1)][x-(size-1)][1] >= size and dp[y-(size-1)][x+(size-1)][0] >= size and min(dp[y-2*(size-1)][x]) > 0:
            max_size = max(max_size, size)
  return max_size

R, C = input_n(int)
table = [list(map(int, input(str))) for _ in range(R)]
print(get_max_size_dp())