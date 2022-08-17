import sys
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

# L
# L L R
# LLR L LRR
# LLRLLRR L LLRRLRR

# 정방향 : 0, 반대방향 : 1
# 정방향일때 L로 돌고, 반대 방향일때 R로 돈다
# 0000000L1111111
# 000L000L000R111 # 반대일땐 역방향으로! (1R0, 0L1)
# 0L1L0L1L0L1R0R1
# LLRLLLRLLLRRLRR

EAST = 0
NORTH = 1
WEST = 2
SOUTH = 3

dy, dx = [0, -1, 0, 1], [1, 0, -1, 0]

LEFT = 1
RIGHT = -1

def turn_d(d, right_or_left):
  return (d + right_or_left)%4

def dfs(y, x, d, g, reverse):
  visited[y][x] = True

  if g == 0:
    return y + dy[d], x + dx[d], d
  
  # 반대일땐 역으로 돈다!
  # if reverse:
  #   mid_y, mid_x, d = dfs(y, x, d, g-1, False)
  #   d = turn_d(d, RIGHT)
  #   end_y, end_x, d = dfs(mid_y, mid_x, d, g-1, True)
  # else:
  #   mid_y, mid_x, d = dfs(y, x, d, g-1, False)
  #   d = turn_d(d, LEFT)
  #   end_y, end_x, d = dfs(mid_y, mid_x, d, g-1, True)

  mid_y, mid_x, d = dfs(y, x, d, g-1, False)
  d = turn_d(d, RIGHT if reverse else LEFT)
  end_y, end_x, d = dfs(mid_y, mid_x, d, g-1, True)

  return end_y, end_x, d

N = input(int)
visited = [[False] * 101 for _ in range(101)]

for _ in range(N):
  x, y, d, g = input_n(int)

  end_y, end_x, _ = dfs(y, x, d, g, False)
  visited[end_y][end_x] = True

cnt_square = 0
for y in range(101-1):
  for x in range(101-1):
    if visited[y][x] and visited[y][x+1] and visited[y+1][x] and visited[y+1][x+1]:
      cnt_square += 1

print(cnt_square)