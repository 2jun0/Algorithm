import sys
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

def get_first_point(max_dist):
  points_log = []
  last_point = points[-1]
  for idx in range(len(points)-1, -1, -1):
    # 하나의 조각이 너무 큼 (max_dist를 만족 시킬 수 없다!)
    if idx-1>=0 and points[idx] - points[idx-1] > max_dist:
      return None

    # 이렇게 자르면 크네? -> 전 위치를 기준으로 자른다.
    elif last_point - points[idx] > max_dist:
      last_point = points[idx+1]
      points_log.append(last_point)
  
  # 너무 많이 잘랐음.
  if len(points_log) > C:
    return None
  
  if len(points_log) < C:
    return points[1]

  return points_log[-1]

def find_dist():
  # max_dist가 작으면 작을 수록 불가능해질 가능성이 높다.
  start = 0
  end = L

  while start < end:
    mid = (start + end) // 2

    if get_first_point(mid):
      end = mid
    else:
      start = mid+1
    
  return end, get_first_point(end)

L, K, C = input_n(int)
points = [0,L]+input_n(int)
points.sort()

dist, first = find_dist()
print(dist, first)