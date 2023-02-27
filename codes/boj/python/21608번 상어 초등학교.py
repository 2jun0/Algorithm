import sys
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

def get_best_pos(N, table, likes):
  '''가장 좋아할 자리 찾아줌'''
  cases = []
  for y in range(N):
    for x in range(N):
      if table[y][x] != 0:
        continue

      zero_cnt = 0
      like_cnt = 0
      for ny, nx in [(y+1,x),(y-1,x),(y,x+1),(y,x-1)]:
        if 0<=ny<N and 0<=nx<N:
          if table[ny][nx] == 0:
            zero_cnt += 1
          elif table[ny][nx] in likes:
            like_cnt+=1

      cases.append((like_cnt, zero_cnt, y,x))
  
  cases.sort(key = lambda case: (-case[0], -case[1], case[2], case[3]))
  return cases[0][2], cases[0][3]

def get_score(table, likes_by_num):
  '''총 만족도 구하기'''
  score = 0
  for y in range(N):
    for x in range(N):
      like_cnt = 0
      for ny, nx in [(y+1,x),(y-1,x),(y,x+1),(y,x-1)]:
        if 0<=ny<N and 0<=nx<N and table[ny][nx] in likes_by_num[table[y][x]]:
          like_cnt+=1
      score += list([0,1,10,100,1000])[like_cnt]
  return score

N = input(int)
table = [[0]*N for _ in range(N)]
likes_by_num = {}

for _ in range(N*N):
  nums = input_n(int)
  num = nums[0]
  likes = nums[1:]
  likes_by_num[num] = likes

  y,x = get_best_pos(N, table, likes)
  table[y][x] = num

print(get_score(table, likes_by_num))