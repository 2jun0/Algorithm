import sys

def input(type_=str):
	return type_(sys.stdin.readline().strip())
def input_n(type_=str):
	return list(map(type_, input().split()))  

def get_masks(M):
  masks = []
  
  def dfs(mask, pos, cnt):
    nonlocal masks
    
    if pos == M:
      masks.append((mask, cnt))
      return
    
    flag = True
    
    if pos > 0 and mask & (1 << (pos-1)): # 옆에 있음
      flag = False
    
    dfs(mask, pos+1, cnt)
    if flag:
      mask |= (1 << pos)
      dfs(mask, pos+1, cnt+1)
  
  dfs(0, 0, 0)
  return masks

C = input(int)
for _ in range(C):
  N, M = input_n(int)
  table = [input() for _ in range(N)]
  dp = [[-1]*(1<<M) for _ in range(N)]
  
  masks = get_masks(M)
  
  for y in range(N):
    for mask, c in masks:
      
      ''' 이 mask가 table에 대해서 유효한지 확인 '''
      flag = True
      for i in range(M):
        if mask & (1 << i) == 0:
          continue
        if table[y][i] == 'x':
          flag = False
          break
      if not flag:
        continue
      
      if y == 0:
        dp[y][mask] = c
        continue
      
      for prev in range(1<<M):
        if dp[y-1][prev] == -1:
          continue
        
        ''' 이 mask가 prev에 대해서 유효한지 확인 '''
        flag = True
        for i in range(M):
          if mask & (1 << i) == 0:
            continue
          if i > 0 and prev & (1 << (i-1)) > 0:
            flag = False
            break
          if i < M-1 and prev & (1 << (i+1)) > 0:
            flag = False
            break
          
        if not flag:
          continue
      
        dp[y][mask] = max(dp[y][mask], dp[y-1][prev] + c)
  print(max(dp[-1]))