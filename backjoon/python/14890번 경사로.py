import sys
sys.setrecursionlimit(10000000) # 재귀 제한 풀기
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

N, L = input_n(int)

table = [input_n(int) for _ in range(N)]

cnt = 0
for i in range(N):
	flat_len = 1

	for j in range(N-1):
		# 같은 높이
		if table[i][j] == table[i][j+1]:
			flat_len += 1
		# 아래로 내려감
		elif table[i][j]-1 == table[i][j+1] and flat_len >= 0:
			flat_len = 1-L # 선계산
		# 위로 올라감
		elif table[i][j]+1 == table[i][j+1] and flat_len >= L:
			flat_len = 1
		else:
			break
	else:
		if flat_len >= 0:
			cnt += 1

for j in range(N):
	flat_len = 1

	for i in range(N-1):
		# 같은 높이
		if table[i][j] == table[i+1][j]:
			flat_len += 1
		# 아래로 내려감
		elif table[i][j]-1 == table[i+1][j] and flat_len >= 0:
			flat_len = 1-L # 선계산
		# 위로 올라감
		elif table[i][j]+1 == table[i+1][j] and flat_len >= L:
			flat_len = 1
		else:
			break
	else:
		if flat_len >= 0:
			cnt += 1

print(cnt)