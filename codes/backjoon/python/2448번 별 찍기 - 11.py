import sys
sys.setrecursionlimit(10000000) # 재귀 제한 풀기
def input(_type=str):
	return _type(sys.stdin.readline().strip())

triangle=[
                (-2,2),
         (-1,1),       (-1,3),
  (0,0), (0,1), (0,2), (0,3), (0,4)]
N = input(int)
result = [[" "]*(2*N) for _ in range(N)]

def func(y, x, width):
  # 밑면은 특이하게 2배가 큼.
  # 가장 작은 삼각형의 밑면이 6개임
  if width==6:
    for ty, tx in triangle: result[ty+y][tx+x] = '*'
    return

  width_nxt = width//2
  height_nxt = width_nxt//2

  func(y, x, width_nxt) # 아래 왼쪽
  func(y, x+width_nxt, width_nxt) # 아래 오른쪽
  func(y-height_nxt, x+width_nxt//2, width_nxt) # 위

# 아래 왼쪽부터 시작.
func(N-1, 0, 2*N-1)
print('\n'.join([''.join(L) for L in result]))