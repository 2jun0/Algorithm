import sys
sys.setrecursionlimit(10000000) # 재귀 제한 풀기
def input(_type=str):
	return _type(sys.stdin.readline().strip())

triangle=[
                (-2,2),
         (-1,1),       (-1,3),
  (0,0), (0,1), (0,2), (0,3), (0,4)
]

big_triangle=[
       (-.5,.5),
  (0,0),       (0,1),
]

N = input(int)
results = [[" "]*(2*N) for _ in range(N)]

def func(y, x, width):
  # 가장 작은 삼각형의 밑면이 6개임
  if width==6:
    for dy, dx in triangle: 
      results[y+dy][x+dx] = '*'
  else:
    width_nxt = width//2
    for dy, dx in big_triangle:
      func(int(y+dy*width_nxt), int(x+dx*width_nxt), width_nxt)

# 아래 왼쪽부터 시작.
func(N-1, 0, 2*N)
print('\n'.join([''.join(L) for L in results]))