import sys
sys.setrecursionlimit(10000000) # 재귀 제한 풀기
INF = 10**8
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))
def print_n(L, join_str=' '):
  for i,l in enumerate(L): print(l, end=join_str if i<len(L)-1 else '\n')
def LL(n,m,d=0): return [[d]*n for _ in range(m)]

N = input(int)
max_t = [0,0,0]
min_t = [0,0,0]
for _ in range(N):
  a,b,c = input_n(int)
  max_t = [
    max(a+max_t[0], a+max_t[1]),
    max(b+max_t[0], b+max_t[1], b+max_t[2]),
    max(c+max_t[1], c+max_t[2])]
  min_t = [
    min(a+min_t[0], a+min_t[1]),
    min(b+min_t[0], b+min_t[1], b+min_t[2]),
    min(c+min_t[1], c+min_t[2])]
print(max(max_t), min(min_t))