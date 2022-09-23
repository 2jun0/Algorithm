INF = 10**10

def dfs(board, aloc, bloc, is_a_turn):
  '''a가 무조건 승리해야 함. -> a가 지는 분기는 INF번 움직임
  - A는 무조건 빠른 경로로 이동
  - B는 무조건 느린 경로로 이동
  '''
  if is_a_turn:
    ay, ax = aloc
    if board[ay][ax] == 0:
      # 어랏 내 발판 어디갔어
      return INF

    board[ay][ax] = 0

    # 이동하지 못한 경우 min(INF + 1, INF) = INF
    min_cnt = INF
    for nxt_y, nxt_x in [(ay-1, ax), (ay+1, ax), (ay, ax-1), (ay, ax+1)]:
      if 0 <= nxt_y < len(board) and 0 <= nxt_x < len(board[0]) and board[nxt_y][nxt_x] == 1:
        min_cnt = min(min_cnt, dfs(board, (nxt_y, nxt_x), bloc, False))

    board[ay][ax] = 1

    return min(min_cnt+1, INF)
  else:
    by, bx = bloc
    if board[by][bx] == 0:
      # 어랏 내 발판 어디갔어 -> 이동못함
      return 0

    board[by][bx] = 0

    # 이동하지 못한 경우 -1 + 1 = 0
    max_cnt = -1
    for nxt_y, nxt_x in [(by-1, bx), (by+1, bx), (by, bx-1), (by, bx+1)]:
      if 0 <= nxt_y < len(board) and 0 <= nxt_x < len(board[0]) and board[nxt_y][nxt_x] == 1:
        max_cnt = max(max_cnt, dfs(board, aloc, (nxt_y, nxt_x), True))

    board[by][bx] = 1

    return max_cnt+1

def solution(board, aloc, bloc):
  return min(dfs(board, bloc, aloc, False), dfs(board, aloc, bloc, True))
  