import sys
def input(type=str):
  return type(sys.stdin.readline().strip())
def input_n(type=str):
  return list(map(type, input().split()))

END_POS = 21

score_for_pos = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 0, 13, 16, 19, 22, 24, 28, 27, 26, 25, 30, 35]
def get_dest(srt, v):
  '''srt에서 v만큼 움직일때 dest값'''
  curr = srt
  for i in range(v):
    if i == 0 and curr == 5:
      curr = 22
    elif i == 0 and curr == 10:
      curr = 25
    elif i == 0 and curr == 15:
      curr = 27

    elif curr == 24:
      curr = 30
    elif curr == 26:
      curr = 30
    elif curr == 32:
      curr = 20

    else:
      curr+=1
    
    if curr == END_POS:
      # 도착 지점 도착 시
      break

  return curr

max_score = 0
def move_dfs(p_idx, pieces, depth, score):
  global max_score

  if depth == len(A):
    return

  nxt_pos = get_dest(pieces[p_idx], A[depth])

  if nxt_pos not in [0, END_POS] and nxt_pos in pieces:
    # 이미 말이 있음 (처음 과 끝은 괜찮음)
    return

  score += score_for_pos[nxt_pos]
  max_score = max(max_score, score)

  pieces[p_idx] = nxt_pos

  for nxt_p_idx in range(4):
    if pieces[nxt_p_idx] != END_POS:
      move_dfs(nxt_p_idx, pieces[::], depth+1, score)

A = input_n(int)
move_dfs(0, [0,0,0,0], 0, 0)

print(max_score)