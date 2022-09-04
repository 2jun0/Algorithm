import sys
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

def get_router_cnt(A, min_dist):
  last_router_pos = A[0]
  router_cnt = 1
  
  for idx in range(1, len(A)):
    # 라우터를 놓을 수 있다면 놓음
    dist = A[idx] - last_router_pos
    if dist >= min_dist:
      last_router_pos = A[idx]
      router_cnt+=1

  return router_cnt

def find_max_dist(A, C):
  # assert e_dist(A, e_dist) <= C <= get_router_cnt(A, s_dist)
  # binary search upper bound
  s_dist = 1
  e_dist = A[-1] - A[0]

  while s_dist < e_dist:
    mid_dist = (s_dist + e_dist) // 2

    if get_router_cnt(A, mid_dist) < C: # <= get_router_cnt(A, s_dist)
      e_dist = mid_dist
    else: # e_dist(A, e_dist) <= C <= get_router_cnt(A, mid_dist)
      s_dist = mid_dist+1
  

  # upper가 없음!
  if e_dist == A[-1] - A[0]:
    return e_dist
  else:
    return e_dist-1

N, C = input_n(int)

A = [input(int) for _ in range(N)]
A.sort()

# refer this [https://st-lab.tistory.com/277]

print(find_max_dist(A, C))