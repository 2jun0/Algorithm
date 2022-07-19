from collections import deque
import sys
INF = 10**10
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

N, K = input_n(int)

def bfs_get_fastest_time():
  costs = [INF]*100001

  q = deque()
  q_nxt = deque()
  t = 0

  q.append(N)

  while q:
    while q:
      x = q.popleft()

      # 1초가 걸리는 것은 q_nxt에 넣고,
      # 0초가 걸리는 것은 바로 *2로 반복문 돌림
      while x <= 100000 and costs[x] > t:
        costs[x] = t

        for t_x in [x-1, x+1]:
          if 0 <= t_x <= 100000:
            q_nxt.append(t_x)
            
        x*=2

    t+=1
    q, q_nxt = q_nxt, q
  
  return costs[K]

print(bfs_get_fastest_time())