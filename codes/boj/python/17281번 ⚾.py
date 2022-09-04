import sys
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

def play():
  global max_score
  order_idx = 0
  score = 0

  for inning in range(N):
    base1, base2, base3 = False, False, False
    out_cnt = 0

    while out_cnt < 3:
      if acts[inning][order[order_idx]] == 0:
        out_cnt += 1
      elif acts[inning][order[order_idx]] == 1:
        score += base3
        base3, base2, base1 = base2, base1, True
      elif acts[inning][order[order_idx]] == 2:
        score += base3 + base2
        base3, base2, base1 = base1, True, False
      elif acts[inning][order[order_idx]] == 3:
        score += base3 + base2 + base1
        base3, base2, base1 = True, False, False
      elif acts[inning][order[order_idx]] == 4:
        score += base3 + base2 + base1 + 1
        base3, base2, base1 = False, False, False
      
      order_idx = (order_idx + 1) % 9 # next player
  
  max_score = max(max_score, score)

visited = [False]*9
visited[0] = True # 첫 주자 위치 고정. 여기선 탐색하지 않는다.
order = [0] * 9
def order_dfs(cnt):
  if cnt == 9:
    play()
    return

  if cnt == 3:
    order_dfs(cnt+1)
    return
  
  for idx in range(1,9):
    if visited[idx]:
      continue
    
    visited[idx] = True
    order[cnt] = idx
    order_dfs(cnt+1)
    visited[idx] = False

N = input(int) # cnt of inning

# act는 아웃, 안타, 2루타, 3루타, 홈런을 나타낸다.
acts = [input_n(int) for _ in range(N)]

max_score = -1
order_dfs(0)

print(max_score)