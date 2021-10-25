import sys
sys.setrecursionlimit(10000000) # 재귀 제한 풀기
INF = 10**10
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))
def print_n(L, join_str=' '):
  for i,l in enumerate(L): print(l, end=join_str if i<len(L)-1 else '\n')
def LL(n,m,d=0): return [[d]*m for _ in range(n)]
def avg(l): return sum(l)/len(l)
def getLRUD(i,j): return [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]

s, N, K, R1, R2, C1, C2 = input_n(int)
powN = [1]
for i in range(1, s):
	powN.append(powN[i-1]*N)

table = LL(R2-R1+1, C2-C1+1)
def mapping(y_st, y_ed, x_st, x_ed):
	for y in range(y_st, y_ed):
		for x in range(x_st, x_ed):
			table[y][x] = 1

for si in range(0, s):
	# 박스 찾기
	y = 0
	ay_st = powN[si]*(N//2-K//2+N*y) if(N%2==1) else powN[si]*(N//2-K//2+N*y)
	ay_ed = ay_st+K*powN[si]
	while ay_st <= R2:
		if R1 < ay_ed:
			x = 0
			ax_st = powN[si]*(N//2-K//2+N*x) if(N%2==1) else powN[si]*(N//2-K//2+N*x)
			ax_ed = ax_st+K*powN[si]
			while ax_st <= C2:
				if C1 < ax_ed:
					mapping(max(ay_st-R1, 0), min(ay_ed-R1, R2-R1+1), max(ax_st-C1, 0), min(ax_ed-C1, C2-C1+1))

				x += 1
				ax_st = powN[si]*(N//2-K//2+N*x) if(N%2==1) else powN[si]*(N//2-K//2+N*x)
				ax_ed = ax_st+K*powN[si]
		y += 1
		ay_st = powN[si]*(N//2-K//2+N*y) if(N%2==1) else powN[si]*(N//2-K//2+N*y)
		ay_ed = ay_st+K*powN[si]
for L in table:
	print_n(L, '')
