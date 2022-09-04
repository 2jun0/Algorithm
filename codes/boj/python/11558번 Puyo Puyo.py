from collections import deque
import sys
def input(_type=str):
	return _type(sys.stdin.readline().strip())

def play():
  def fall_down():
    for x in range(6):
      from_y = 11
      to_y = 11
      while from_y >= 0:
        if table[from_y][x] != '.':
          table[to_y][x], table[from_y][x] = table[from_y][x], table[to_y][x]
          to_y -= 1
        from_y -= 1

  def get_relatives_dfs(y, x, visited):
    relatives = deque([(y,x)])
    visited[y][x] = True
    for n_y, n_x in [(y-1,x),(y+1,x),(y,x-1),(y,x+1)]:
      if 0<=n_y<12 and 0<=n_x<6 and table[n_y][n_x] == table[y][x] and not visited[n_y][n_x]:
        relatives.extend(get_relatives_dfs(n_y, n_x, visited))
      
    return relatives

  def try_pop(y, x): # 뿌요 터뜨리기
    relatives = get_relatives_dfs(y, x, [[False]*6 for _ in range(12)])
    if len(relatives) >= 4:
      for y, x in relatives:
        table[y][x] = '.'
      return True
    return False

  combo = 0
  while True:
    is_poped = False

    for y in range(12):
      for x in range(6):
        if table[y][x] != '.':
          if try_pop(y,x):
            is_poped = True
    
    if is_poped:
      combo+=1
      fall_down()
    else:
      break
  
  return combo

table = [list(map(str, input())) for _ in range(12)]
print(play())