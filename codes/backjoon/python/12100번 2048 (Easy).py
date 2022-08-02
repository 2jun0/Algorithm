from collections import deque
import sys
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

N = input(int)
table = [input_n(int) for _ in range(N)]

LEFT, RIGHT, UP, DOWN = 0, 1, 2, 3

def go(t,d):
  nxt_t = [[0]*N for _ in range(N)]

  # flag = 이전에 합쳐졌는지 여부
  if d==LEFT: 
    for y in range(N):
      flag, nxt_x = False, 0
      for cur_x in range(N):
        # 숫자가 0인경우 (패스)
        if t[y][cur_x] == 0: continue
        # 이전에 합쳐진 경우 & 처음일 경우 & 이전의 숫자와 같은 경우
        if not flag and nxt_x-1>=0 and t[y][cur_x] == nxt_t[y][nxt_x-1]:
          nxt_t[y][nxt_x-1] = 2*t[y][cur_x]
          flag = True
        else: # 이전의 숫자와 다른 경우
          nxt_t[y][nxt_x] = t[y][cur_x]
          nxt_x+=1
          flag = False
  elif d==RIGHT:
    for y in range(N):
      flag, nxt_x = False, N-1
      for cur_x in range(N-1, -1, -1):
        # 숫자가 0인경우 (패스)
        if t[y][cur_x] == 0: continue
        # 이전에 합쳐진 경우 & 처음일 경우 & 이전의 숫자와 같은 경우
        if not flag and nxt_x+1<N and t[y][cur_x] == nxt_t[y][nxt_x+1]:
          nxt_t[y][nxt_x+1] = 2*t[y][cur_x]
          flag = True
        else: # 이전의 숫자와 다른 경우
          nxt_t[y][nxt_x] = t[y][cur_x]
          nxt_x-=1
          flag = False
  elif d==UP: 
    for x in range(N):
      flag, nxt_y = False, 0
      for y in range(N):
        # 숫자가 0인경우 (패스)
        if t[y][x] == 0: continue
        # 이전에 합쳐진 경우 & 처음일 경우 & 이전의 숫자와 같은 경우
        if not flag and nxt_y-1>=0 and t[y][x] == nxt_t[nxt_y-1][x]:
          nxt_t[nxt_y-1][x] = 2*t[y][x]
          flag = True
        else: # 이전의 숫자와 다른 경우
          nxt_t[nxt_y][x] = t[y][x]
          nxt_y+=1
          flag = False
  elif d==DOWN:
    for x in range(N):
      flag, nxt_y = False, N-1
      for y in range(N-1, -1, -1):
        # 숫자가 0인경우 (패스)
        if t[y][x] == 0: continue
        # 이전에 합쳐진 경우 & 처음일 경우 & 이전의 숫자와 같은 경우
        if not flag and nxt_y+1<N and t[y][x] == nxt_t[nxt_y+1][x]:
          nxt_t[nxt_y+1][x] = 2*t[y][x]
          flag = True
        else: # 이전의 숫자와 다른 경우
          nxt_t[nxt_y][x] = t[y][x]
          nxt_y-=1
          flag = False
  return nxt_t

max_v = 0

q = deque([(0,table)])
while q:
  lv, t = q.popleft()
  max_v = max(max_v, max([max(l) for l in t]))

  if lv+1 <= 5:
    q.append((lv+1, go(t,LEFT)))
    q.append((lv+1, go(t,RIGHT)))
    q.append((lv+1, go(t,UP)))
    q.append((lv+1, go(t,DOWN)))
print(max_v)