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

N = input(int)
table = LL(N,N)

for i in range(N):
  for j, c in enumerate(input(str)):
    table[i][j] = int(c)

# i에서 visited만큼 방문하면 cost 몇임?
dp_visited = LL(1<<(N+1), N)
# i에서 cost원 쓰면 최대 몇명 팔 수 있음?
dp_cost = LL(10, N)
