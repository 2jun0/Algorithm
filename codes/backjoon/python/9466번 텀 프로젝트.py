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

# 이 문제는 그래프의 루프를 찾는 문제임.
# 따라서 done과 visited 리스트를 이용한다.

T = input(int)
for _ in range(T):
  # 헷갈리니 index를 1부터 한다.
	n = input(int)+1
	# A[index] = index번째 학생이 선택한 학생
	A = [0]+input_n(int)
	
	cnt = 0 # 팀을 이룬 학생의 수
	visited = [False]*n # DFS노드 방문여부
	done = [False]*n # DFS 탐색 종료 여부

	def DFS(x):
		global cnt
		visited[x] = True # 방문함
		next = A[x] # 선택한 학생
		if not visited[next]: # 선택한 학생이 아직 방문하지 않았다면 DFS 탐색
			DFS(next)

		# 순환 그래프 탐색
		elif not done[next]:
			circle_x = next
			cnt += 1
			while circle_x != x: 
				circle_x = A[circle_x]
				cnt += 1

		# 한번 탐색한 노드는 다시 보지 않음.
		done[x] = True

	for i in range(1,n):
		if not done[i]:
			DFS(i)

	print(done)

	print(n-cnt-1)