import sys
sys.setrecursionlimit(10000000) # 재귀 제한 풀기

def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

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
		visited[x] = True # 노드 탐색 시작
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

		# 노드 탐색 끝
		done[x] = True

	for i in range(1,n):
		if not visited[i]:
			DFS(i)

	print(n-cnt-1)