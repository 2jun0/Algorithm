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
	
T = input(int)
for _ in range(T):
	n = input(int)+1
	A = [0]+input_n(int)
	
	cnt = 0
	visited = [False]*n
	done = [False]*n
	def DFS(x):
		global cnt
		visited[x] = True
		next = A[x]
		if not visited[next]:
			DFS(next)
		elif not done[next]:
			y = next
			cnt += 1
			while y != x: 
				y = A[y]
				cnt += 1

		done[x] = True

	for i in range(1,n):
		if not visited[i]:
			DFS(i)

	print(n-cnt-1)