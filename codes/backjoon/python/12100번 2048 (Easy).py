import sys
sys.setrecursionlimit(10000000) # 재귀 제한 풀기
INF = 10**10
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))
def print_n(L, join_str=' '):
  for i,l in enumerate(L): print(l, end=join_str if i<len(L)-1 else '\n')
def LL(n,m,d=0): return [[d]*n for _ in range(m)]
def avg(l): return sum(l)/len(l)

N = input(int)
table = [input_n(int) for _ in range(N)]

LEFT, RIGHT, UP, DOWN = 0, 1, 2, 3
s = [table]

def go(t,d):
  nxt_t = LL(N,N)
  
  if d==LEFT: 
    for y in range(N):
      flag, nxt_x = False, 0
      for cur_x in range(N):
        # 숫자가 0인경우 (패스)
        if t[y][cur_x] == 0: continue
        # 뒤의 숫자와 같은 경우 or 뒤의 숫자따위 없다!
        if not flag and nxt_x-1>=0 and t[y][cur_x] == nxt_t[y][nxt_x-1]:
          nxt_t[y][nxt_x-1] = 2*t[y][cur_x]
          flag = True
        # 뒤의 숫자와 다른 경우
        else:
          nxt_t[y][nxt_x] = t[y][cur_x]
          nxt_x+=1
          flag = False
  elif d==RIGHT:
    for y in range(N):
      flag, nxt_x = False, N-1
      for cur_x in range(N-1, -1, -1):
        # 숫자가 0인경우 (패스)
        if t[y][cur_x] == 0: continue
        # 뒤의 숫자와 같은 경우 or 뒤의 숫자따위 없다!
        if not flag and nxt_x+1<N and t[y][cur_x] == nxt_t[y][nxt_x+1]:
          nxt_t[y][nxt_x+1] = 2*t[y][cur_x]
          flag = True
        # 뒤의 숫자와 다른 경우
        else:
          nxt_t[y][nxt_x] = t[y][cur_x]
          nxt_x-=1
          flag = False
  elif d==UP: 
    for x in range(N):
      flag, nxt_y = False, 0
      for cur_y in range(N):
        # 숫자가 0인경우 (패스)
        if t[cur_y][x] == 0: continue
        # 뒤의 숫자와 같은 경우 or 뒤의 숫자따위 없다!
        if not flag and nxt_y-1>=0 and t[cur_y][x] == nxt_t[nxt_y-1][x]:
          nxt_t[nxt_y-1][x] = 2*t[cur_y][x]
          flag = True
        # 뒤의 숫자와 다른 경우
        else:
          nxt_t[nxt_y][x] = t[cur_y][x]
          nxt_y+=1
          flag = False
  elif d==DOWN:
    for x in range(N):
      flag, nxt_y = False, N-1
      for cur_y in range(N-1, -1, -1):
        # 숫자가 0인경우 (패스)
        if t[cur_y][x] == 0: continue
        # 뒤의 숫자와 같은 경우 or 뒤의 숫자따위 없다!
        if not flag and nxt_y+1<N and t[cur_y][x] == nxt_t[nxt_y+1][x]:
          nxt_t[nxt_y+1][x] = 2*t[cur_y][x]
          flag = True
        # 뒤의 숫자와 다른 경우
        else:
          nxt_t[nxt_y][x] = t[cur_y][x]
          nxt_y-=1
          flag = False
  return nxt_t

max_v = 0

s = [(0,table)]
while len(s) > 0:
  lv, t = s.pop()
  max_v = max([max_v]+[max(l) for l in t])
  if lv >= 5: continue
  s.append((lv+1, go(t,LEFT)))
  s.append((lv+1, go(t,RIGHT)))
  s.append((lv+1, go(t,UP)))
  s.append((lv+1, go(t,DOWN)))
print(max_v)