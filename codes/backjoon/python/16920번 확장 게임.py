from collections import deque
import sys
INF = 10**10
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

N, M, P = input_n(int)
S = input_n(int)
table = [list(map(str,input())) for _ in range(N)]

def bfs(table):
  ques = [deque() for _ in range(P)]
  ques_nxt = [deque() for _ in range(P)]

  # 플레이어 별 성 개수
  cnts = [0]*P

  # cnts 초기화
  for i in range(N):
    for j in range(M):
      if table[i][j] != '.' and table[i][j] != '#':
        p = int(table[i][j])-1
        cnts[p] += 1
        ques[p].append((S[p],i,j))

  while True:
    is_empty = True

    for p in range(P):
      if ques[p]:
        is_empty = False

      while ques[p]:
        remain,i,j = ques[p].popleft()
        remain-=1

        for t_i, t_j in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
          if 0<=t_i<N and 0<=t_j<M:
            # 빈 칸인 경우 성 건설
            if table[t_i][t_j] == '.':
              cnts[p] += 1
              table[t_i][t_j] = str(p+1)
              # 빈 칸이면서 움직일 수 있다면
              # 현재 레벨로 반복
              if remain > 0:
                ques[p].append((remain,t_i,t_j))
              # 움직일 수 없다면
              # 다음 레벨로 넘기기
              else:
                ques_nxt[p].append((S[p], t_i, t_j))

    if is_empty:
      return cnts

    ques, ques_nxt = ques_nxt, ques

print(' '.join(map(str, bfs(table))))
