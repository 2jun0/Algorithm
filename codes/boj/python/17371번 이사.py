import sys
INF = 10**10
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))
def print_n(L, join_str=' '):
  for i,l in enumerate(L): print(l, end=join_str if i<len(L)-1 else '\n')
def LL(n,m,d=0): return [[d]*n for _ in range(m)]
def avg(l): return sum(l)/len(l)
def getLRUD(i,j): return [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]

N = input(int)
A = [input_n(int) for _ in range(N)]

min_max_d = INF
min_max_d_a = None
for ax, ay in A:
	max_d = -INF
	for bx, by in A:
		d = (bx - ax) ** 2 + (by - ay) ** 2
		if max_d < d:
			max_d = d
	if max_d < min_max_d:
		min_max_d = max_d
		min_max_d_a = (ax, ay)

print(min_max_d_a[0], min_max_d_a[1])