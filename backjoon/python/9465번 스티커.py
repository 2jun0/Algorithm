import sys
sys.setrecursionlimit(10000000) # 재귀 제한 풀기
INF = 10**8
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))
def print_n(L, join_str=' '):
  for l in L: print(l, end=join_str)

T = input(int)
for _ in range(T):
  n = input(int)
  scores = [input_n(int), input_n(int)]

  for i in range(1,n):
    pre_s0, pre_s1 = scores[0][i-1], scores[1][i-1]
    s0 = max(pre_s1+scores[0][i], pre_s0)
    s1 = max(pre_s0+scores[1][i], pre_s1)
    scores[0][i], scores[1][i] = s0, s1
  print(max(scores[0][-1], scores[1][-1]))