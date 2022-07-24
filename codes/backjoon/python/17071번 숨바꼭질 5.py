from collections import deque
import sys
INF = 10**10
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

N, K = input_n(int)

def bfs():
  # 수빈이는 이미 밟았던 땅을 홀/짝 기준으로 다시 밟음.
  # (x+1, x-1) 때문임.
  # 고로, 한번 갔던 땅은 다시 갈 필요가 없다.
  costs = [[INF] * 500001 for _ in range(2)]
  # x, time
  q = deque()

  costs[0][N] = 0
  q.append((N, 0))
  
  while q:
    x, t = q.popleft()

    for t_x in [x*2, x+1, x-1]:

      if 0<=t_x<=500000 and costs[(t+1)%2][t_x] == INF:
        costs[(t+1)%2][t_x] = t+1
        q.append((t_x, t+1))
  
  t = 0
  k = K
  while k <= 500000:
    # 수빈이가 밟았던 땅을 동생이 밟는다면 동생이 도착했을 때 만남.
    #
    # 단, 아래의 조건을 만족해야함.
    # 1. 동생이 먼저 가면 안됨. (수빈이가 먼저 와 있어야 함)
    # 2. 홀짝 조건을 만족해야 함.
    if t >= costs[t%2][k]:
      return t

    t+=1
    k+=t

  return -1

print(bfs())