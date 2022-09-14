'''
4*(20*20)*(20*20) = 640,000
'''
def rotate_right(key):
  M = len(key)
  new_key = [[0]*M for _ in range(M)]

  for y in range(M):
    for x in range(M):
      new_key[x][M-1-y] = key[y][x]
  
  return new_key

def can_unlock(key, lock, srt_k_y, srt_k_x, srt_l_y, srt_l_x):
  M = len(key)
  N = len(lock)

  remain_0 = N*N - sum(sum(L) for L in lock)

  k_y, l_y = srt_k_y, srt_l_y
  while k_y < M and l_y < N:
    k_x, l_x = srt_k_x, srt_l_x
    while k_x < M and l_x < N:
      if key[k_y][k_x] == 1 and lock[l_y][l_x] == 1:
        # 홈에 들어가지 않는다!
        return False
      
      if key[k_y][k_x] == 1 and lock[l_y][l_x] == 0:
        # 홈에 들어갔다!
        remain_0 -= 1

      k_x, l_x = k_x+1, l_x+1
    
    k_y, l_y = k_y+1, l_y+1

  return remain_0 == 0

def solution(key, lock):
  N = len(lock)

  for _ in range(4):
    for srt_k_y in range(N):
      for srt_k_x in range(N):
        for srt_l_y in range(N):
          for srt_l_x in range(N):
            if can_unlock(key, lock, srt_k_y, srt_k_x, srt_l_y, srt_l_x):
              return True

    key = rotate_right(key)

  return False