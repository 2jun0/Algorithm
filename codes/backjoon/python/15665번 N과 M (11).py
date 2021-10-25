import sys
sys.setrecursionlimit(10000000) # 재귀 제한 풀기
INF = 10**8
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))
def print_n(L, join_str=' '):
  for i,l in enumerate(L): print(l, end=join_str if i<len(L)-1 else '\n')

N, M = input_n(int)
A = input_n(int)
A = list(set(A))
A.sort()
result = [0]*M
def func(d):
  if d==M:
    print_n(result)
    return
  for i, a in enumerate(A):
    result[d] = a
    func(d+1)
func(0)
