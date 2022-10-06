import sys
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

def create_is_corner(N, tor_y, tor_x):
  '''코너인지 확인하는 2차원 배열을 반환'''
  is_corner = [[False]*N for _ in range(N)]

  for y, x, dy, dx in [
      (tor_y, tor_x-1, -1, -1),
      (tor_y+1, tor_x-1, 1, -1), 
      (tor_y-1, tor_x+1, -1, 1), 
      (tor_y+1, tor_x+1, 1, 1)]:
    while 0<=y<N and 0<=x<N:
      is_corner[y][x] = True
      y, x = y + dy, x + dx
  
  return is_corner

def spread_sand(table, src_y, src_x, d):
  '''모래 흩뿌리기
  - Returns: 격자 밖으로 벗어난 모래 양
  '''
  sand_v = table[src_y][src_x]
  table[src_y][src_x] = 0

  out_v = 0
  remain_v = sand_v
  alpha_y, alpha_x = None, None

  for sp_y in range(5):
    for sp_x in range(5):
      dst_y = src_y + sp_y - 2
      dst_x = src_x + sp_x - 2

      if spread_table[d][sp_y][sp_x] == .65:
        alpha_y, alpha_x = dst_y, dst_x
        continue

      v = int(sand_v * spread_table[d][sp_y][sp_x])
      remain_v -= v

      if 0<=dst_y<N and 0<=dst_x<N:
        table[dst_y][dst_x] += v
      else:
        out_v += v

  if 0<=alpha_y<N and 0<=alpha_x<N:
    table[alpha_y][alpha_x] += remain_v
  else:
    out_v += remain_v

  return out_v
  
tor_dy = [-1,0,1,0]
tor_dx = [0,1,0,-1]
spread_table = [
  [
    [.00,.00,.05,.00,.00],
    [.00,.10,.65,.10,.00],
    [.02,.07,.00,.07,.02],
    [.00,.01,.00,.01,.00],
    [.00,.00,.00,.00,.00],
  ],
  [
    [.00,.00,.02,.00,.00],
    [.00,.01,.07,.10,.00],
    [.00,.00,.00,.65,.05],
    [.00,.01,.07,.10,.00],
    [.00,.00,.02,.00,.00],
  ],
  [
    [.00,.00,.00,.00,.00],
    [.00,.01,.00,.01,.00],
    [.02,.07,.00,.07,.02],
    [.00,.10,.65,.10,.00],
    [.00,.00,.05,.00,.00],
  ],
  [
    [.00,.00,.02,.00,.00],
    [.00,.10,.07,.01,.00],
    [.05,.65,.00,.00,.00],
    [.00,.10,.07,.01,.00],
    [.00,.00,.02,.00,.00],
  ],
]

N = input(int)
table = [input_n(int) for _ in range(N)]

tor_y, tor_x = N//2, N//2
tor_d = 3

is_corner = create_is_corner(N, tor_y, tor_x)
out_v = 0

while 0<=tor_y<N and 0<=tor_x<N:
  # (0,0) 까지 순회

  out_v += spread_sand(table, tor_y, tor_x, tor_d)

  if is_corner[tor_y][tor_x]:
    # 현재 좌표가 코너라면 반시계 회전
    tor_d = (tor_d - 1) % 4

  tor_y, tor_x = tor_y + tor_dy[tor_d], tor_x + tor_dx[tor_d]

# print(table)
print(out_v)