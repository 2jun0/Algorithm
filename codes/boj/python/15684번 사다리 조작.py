import sys
INF = 10**10
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

def check_ladder():
  for row in range(N):
    curr = row
    for col in range(H):
      if curr<N-1 and has_lines[col][curr]:
        curr+=1
      elif 0<=curr-1 and has_lines[col][curr-1]:
        curr-=1

    if curr != row:
      return False
    
  return True

def dfs(col, cnt):
  global min_cnt

  if check_ladder():
    min_cnt = min(min_cnt, cnt)
    return 

  if cnt < 3:
    for n_col in range(col, H):
      for n_row in range(N-1):
        if min_cnt <= cnt+1:
          return

        if has_lines[n_col][n_row]: continue
        if 0<=n_row-1 and has_lines[n_col][n_row-1]: continue
        if n_row+1<N-1 and has_lines[n_col][n_row+1]: continue

        has_lines[n_col][n_row] = True
        dfs(n_col, cnt+1)
        has_lines[n_col][n_row] = False

N, M, H = input_n(int)
has_lines = [[False]*(N-1) for _ in range(H)]
for _ in range(M):
  a, b = input_n(int)
  has_lines[a-1][b-1] = True

min_cnt = INF
dfs(0,0)
print(min_cnt if min_cnt != INF else -1)