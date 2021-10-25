import sys

def input(_type=str):
	return _type(sys.stdin.readline().rstrip())
def input_n(_type):
	return list(map(_type, input().split()))

INF = 10**8

N, M, B = input_n(int)
A = [input_n(int) for _ in range(N)]

sum = 0
for L in A:
  for a in L:
    sum+=a

def p(x):
  """x높이로 땅을 고르게 할때 얼마의 시간이 걸리는가"""
  time = 0
  b_cnt = B
  for i in range(N):
    for j in range(M):
      if x < A[i][j]:
        gap = A[i][j]-x
        b_cnt += gap
        time += gap*2
      elif x > A[i][j]:
        gap = x - A[i][j]
        b_cnt -= gap
        time += gap
  if b_cnt < 0:
    return INF
  return time

min_time = INF
good_x = 0
visited = [False] * 257
s = [sum//(M*N)]
while len(s) > 0:
  x = s.pop()
  if (x < 0 or x > 256) or visited[x]:
    continue
  visited[x] = True
  p_x = p(x)
  if p_x < min_time or (p_x == min_time and x > good_x):
    good_x = x
    min_time = p_x
    s.append(x-1)
    s.append(x+1)

print(min_time, good_x)