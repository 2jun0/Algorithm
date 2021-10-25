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

class Node:
	def __init__(self, name):
		self.name = name
		self.childs = {}

N = input(int)
root = Node('root')
for _ in range(N):
	L = input_n()
	
	last_node = root
	for i in range(1, len(L)):
		if L[i] not in last_node.childs.keys():
			last_node.childs[L[i]] = Node(L[i])
		last_node = last_node.childs[L[i]]

s = [(-1,root)]
while len(s) > 0:
	lv, node =  s.pop()
	if lv >= 0: print('--'*lv+node.name)
	for name in sorted(node.childs.keys(), reverse=True):
		s.append((lv+1, node.childs[name]))
