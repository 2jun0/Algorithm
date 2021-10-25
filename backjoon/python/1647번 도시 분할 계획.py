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

class Node:
	def __init__(self):
		self.p = self
	def find(self):
		if self.p!=self:
			self.p = self.p.find()
		return self.p
	def union(self, n):
		n.find().p = self.find()

N, M = input_n(int)
nodes = [Node() for _ in range(N)]
L = []
for _ in range(M):
	a,b,c = input_n(int)
	L.append((c,a-1,b-1))

L.sort()
sum_v = 0
last = 0
for c,a,b in L:
	if nodes[a].find() != nodes[b].find():
		nodes[a].union(nodes[b])
		sum_v += c
		last = c
print(sum_v-last)