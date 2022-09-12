import sys
def input(type=str):
  return type(sys.stdin.readline().strip())
def input_n(type=str):
  return list(map(type, input().split()))

INF = 10**10

def get_pos_cnt_by_max_dist(max_dist):
  cnt = 0
  last_pos = 0
  for idx in range(N):
    if pos[idx] - last_pos > max_dist:
      cnt += (pos[idx] - last_pos) // max_dist
      if (pos[idx] - last_pos) % max_dist == 0:
        cnt -= 1

    last_pos = pos[idx]
  
  if L - last_pos > max_dist:
    cnt += (L - last_pos) // max_dist
    if (L - last_pos) % max_dist == 0:
      cnt -= 1

  return cnt

def find_min_max_dist():
  start = 1
  end = L

  while start < end:
    mid = (start + end) // 2
    if get_pos_cnt_by_max_dist(mid) <= M:
      end = mid
    else:
      start = mid + 1

  return end

N, M, L = input_n(int)
pos = input_n(int)

pos.sort()

print(find_min_max_dist())