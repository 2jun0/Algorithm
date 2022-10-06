from collections import deque
from copy import deepcopy
import sys
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

def copy_transpose_block(src_table, dst_table, srt_src_y, srt_src_x, srt_dst_y, srt_dst_x, size):
  '''
  - src_table[srt_src_y:srt_src_y+size][srt_src_x:srt_src_x+size]^T를 
  - dst_table[srt_dst_y:srt_dst_y+size][srt_dst_x:srt_dst_x+size]로 복사
  '''
  for y in range(size):
    for x in range(size):
      src_y, src_x = y + srt_src_y, x + srt_src_x
      dst_y, dst_x = x + srt_dst_y, size-1-y + srt_dst_x

      dst_table[dst_y][dst_x] = src_table[src_y][src_x]

def turn_dfs(table, nxt_table, srt_y, srt_x, curr_size, target_size):
  '''
  - curr_zie : 현재 level의 size
  - target_size : 2**L
  - area : UP_LEFT | UP_RIGHT | DOWN_LEFT | DOWN_RIGHT
  '''
  if curr_size == target_size:
    # 선택된 격자의 부분격자를 시계방향 90도로 돌림
    if curr_size == 1:
      # 격자 크기가 1개인 경우엔 부분격자로 나눌 수 없음.
      nxt_table[srt_y][srt_x] = table[srt_y][srt_x]
    else:
      nxt_size = curr_size // 2
      copy_transpose_block(table, nxt_table, srt_y, srt_x, srt_y, srt_x+nxt_size, nxt_size)
      copy_transpose_block(table, nxt_table, srt_y+nxt_size, srt_x, srt_y, srt_x, nxt_size)
      copy_transpose_block(table, nxt_table, srt_y, srt_x+nxt_size, srt_y+nxt_size, srt_x+nxt_size, nxt_size)
      copy_transpose_block(table, nxt_table, srt_y+nxt_size, srt_x+nxt_size, srt_y+nxt_size, srt_x, nxt_size)

  else:
    # 다음 크기의 격차 찾기
    assert curr_size > target_size

    nxt_size = curr_size // 2
    turn_dfs(table, nxt_table, srt_y, srt_x, nxt_size, target_size)
    turn_dfs(table, nxt_table, srt_y, srt_x+nxt_size, nxt_size, target_size)
    turn_dfs(table, nxt_table, srt_y+nxt_size, srt_x, nxt_size, target_size)
    turn_dfs(table, nxt_table, srt_y+nxt_size, srt_x+nxt_size, nxt_size, target_size)

def melt(table):
  '''table내 얼음을 녹임
  - 얼음은 인접한 얼음의 수가 2개 이하일때 녹음
  '''
  nxt_table = deepcopy(table)

  for y in range(2**N):
    for x in range(2**N):
      if nxt_table[y][x] <= 0:
        continue

      adj_ice_cnt = 0
      for adj_y, adj_x in [(y-1,x),(y+1,x),(y,x-1),(y,x+1)]:
        if 0<=adj_y<2**N and 0<=adj_x<2**N and table[adj_y][adj_x] > 0:
          adj_ice_cnt += 1

      if adj_ice_cnt <= 2:
        nxt_table[y][x] -= 1
  
  return nxt_table

def get_chunk_sizes_dfs(table):
  '''덩어리들의 각 얼음 개수를 구하는 함수'''
  visited = [[False]*(2**N) for _ in range(2**N)]

  def get_chunk_size_bfs(srt_y, srt_x):
    '''srt_y, srt_x가 속해있는 덩어리의 크기 구하기'''
    assert not visited[srt_y][srt_x] and table[srt_y][srt_x] > 0

    visited[srt_y][srt_x] = True
    q = deque([(srt_y, srt_x)])
    cnt = 0

    while q:
      y, x = q.popleft()
      cnt += 1

      for adj_y, adj_x in [(y-1,x),(y+1,x),(y,x-1),(y,x+1)]:
        if 0<=adj_y<2**N and 0<=adj_x<2**N and table[adj_y][adj_x] > 0 and not visited[adj_y][adj_x]:
          visited[adj_y][adj_x] = True
          q.append((adj_y, adj_x))

    return cnt

  chunk_sizes = []
  for y in range(2**N):
    for x in range(2**N):
      if not visited[y][x] and table[y][x] > 0:
        chunk_sizes.append(get_chunk_size_bfs(y, x))
  
  return chunk_sizes

N, Q = input_n(int)
table = [input_n(int) for _ in range(2**N)]
Ls = input_n(int)

for L in Ls:
  nxt_table = [[0]*(2**N) for _ in range(2**N)]
  turn_dfs(table, nxt_table, 0, 0, 2**N, 2**L)
  table = nxt_table
  table = melt(table)

# for line in table:
#   print(line)

print(sum(sum(line) for line in table))
chunk_sizes = get_chunk_sizes_dfs(table)
# print(chunk_sizes)
print(max(chunk_sizes) if chunk_sizes else 0)