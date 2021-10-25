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

class LCANode:
	def __init__(self, idx):
		self.idx = idx
		self.ps = []
	def find(self, d):
		i = 2**20
		while len(ps)
		self.ps[]

N = input(int)

LCA = [[] for _ in range(N+1)]
LCAD = [[] for _ in range(N+1)]
for _ in range(N):
	a,b = input_n(int)
	if len(LCA[b]) > 0: a,b = b,a

	LCA[b].append(a)
	while LCA[a]
	for 
