import sys
sys.setrecursionlimit(10000000) # 재귀 제한 풀기
INF = 10**8
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))
def print_n(L, join_str=' '):
  for i,l in enumerate(L): print(l, end=join_str if i<len(L)-1 else '\n')

triangle=[
                (-2,2),
         (-1,1),       (-1,3),
  (0,0), (0,1), (0,2), (0,3), (0,4)]
N = input(int)
result = [[" "]*(2*N) for _ in range(N)]
def func(y, x, width):
  if width==6:
    for ty, tx in triangle: result[ty+y][tx+x] = '*'
    return

  wd2 = width//2
  hd2 = wd2//2
  func(y,x,wd2)
  func(y,x+wd2,wd2)
  func(y-hd2,x+hd2,wd2)
func(N-1, 0, 2*N)
print('\n'.join([''.join(L) for L in result]))