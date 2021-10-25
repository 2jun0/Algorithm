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
A = list(set(input_n(int)))
A.sort()
ocuppied = [0]*len(A)
result = [0]*M
def func(d):
  if d==M:
    print_n(result)
    return
  for i, a in enumerate(A):
    if ocuppied[i] >= M or (d>0 and result[d-1]>a): continue
    ocuppied[i] +=1
    result[d] = a
    func(d+1)
    ocuppied[i] -=1
func(0)