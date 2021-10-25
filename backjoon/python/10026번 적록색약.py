import sys

INF = 10**8
def input(_type=str):
	return _type(sys.stdin.readline().rstrip())
def input_n(_type=str):
	return list(map(_type, input().split()))
def print_n(L):
  s = ''
  for l in L: s+='{} '.format(l)
  print(s[:-1])

N = input(int)
table = [input() for _ in range(N)]


def rgb():
  cnt = 0
  visited = [[False]*N for _ in range(N)]

  def ok(i,j,color):
    return (0<=i<N and 0<=j<N) and (not visited[i][j] and table[i][j]==color)

  s = []
  for _i in range(N):
    for _j in range(N):
      if not visited[_i][_j]:
        cnt +=1
        s.append((_i,_j,table[_i][_j]))
        
        while len(s) > 0:
          i, j, color = s.pop()
          if not ok(i,j,color): continue
          visited[i][j] = True

          s.extend([(i-1,j,color), (i+1,j,color), (i,j-1,color), (i,j+1,color)])

  return cnt

def rb():
  cnt = 0
  visited = [[False]*N for _ in range(N)]

  def color_eq(c1, c2):
    if (c1=='B' and c2!='B') or (c1!='B' and c2=='B'): return False
    else: return True
  def ok(i,j,color):
    return (0<=i<N and 0<=j<N) and (not visited[i][j] and color_eq(table[i][j], color))

  s = []
  for _i in range(N):
    for _j in range(N):
      if not visited[_i][_j]:
        cnt +=1
        s.append((_i,_j,table[_i][_j]))
        
        while len(s) > 0:
          i, j, color = s.pop()
          if not ok(i,j,color): continue
          visited[i][j] = True

          s.extend([(i-1,j,color), (i+1,j,color), (i,j-1,color), (i,j+1,color)])

  return cnt
print(rgb(), rb())