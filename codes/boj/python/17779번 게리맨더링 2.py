import sys
def input(type=str):
  return type(sys.stdin.readline().strip())
def input_n(type=str):
  return list(map(type, input().split()))

def get_populations_for_district(x, y, d1, d2):
  ''' 선거구 별 인구수 구하기 

    구역 5의 범위는 아래와 같다.
    x+|y-c| <= r <= x+d1+d2-|y+d2-d1-c|
    y-d1+|x+d1-r| <= c <= y+d2-|x+d2-r|
  '''
  districts = [0 for _ in range(5)]

  for c in range(1,N+1):
    for r in range(1,N+1):
      if x+abs(y-c) <= r <= x+d1+d2-abs(y-d1+d2-c) \
        and y-d1+abs(x+d1-r) <= c <= y+d2-abs(x+d2-r):
        districts[4] += A[r-1][c-1]
      elif r < x+d1 and c <= y:
        districts[0] += A[r-1][c-1]
      elif r <= x+d2 and y < c:
        districts[1] += A[r-1][c-1]
      elif x+d1 <= r and c < y-d1+d2:
        districts[2] += A[r-1][c-1]
      elif x+d2 < r and y-d1+d2 <= c:
        districts[3] += A[r-1][c-1]
  
  return districts

# 1 <= y-d1 < y < y+d2 <= N
# x < x+d1+d2 <= N
def get_min_diff_every_boundary():
  ''' 모든 경계선에 대한 최소 구역인구 차이 구하기 '''
  min_diff = 10**10
  for y in range(1,N+1):
    for x in range(1,N+1):
      for d1 in range(1,N+1):
        for d2 in range(1,N+1):
          if x+d1+d2<=N and 1<=y+d2-d1<=N and x+d1<=N and 1<=y-d1 and x+d2<=N and y+d2<=N:
            districts = get_populations_for_district(x,y,d1,d2)
            min_diff = min(min_diff, max(districts) - min(districts))
          
  return min_diff

N = input(int)
A = [input_n(int) for _ in range(N)]

print(get_min_diff_every_boundary())