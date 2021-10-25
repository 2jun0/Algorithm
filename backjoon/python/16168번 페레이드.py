import sys
sys.setrecursionlimit(10000000) # 재귀 제한 풀기

def input(_type=str):
	return _type(sys.stdin.readline().rstrip())
def input_n(_type):
	return list(map(_type, input().split()))

V, E = input_n(int)

# 오일러 경로나, 오일러 회로일 경우 YES 아니면 NO
# 오일러 경로 : 홀수 간선 정점 0개
# 오일러 회로 : 홀수 간선 정점 2개

from_tos = [[] for _ in range(V+1)]

for _ in range(E):
  Va, Vb = input_n(int)

  from_tos[Va].append(Vb)
  from_tos[Vb].append(Va)

# 중복제거
# for i, from_to in enumerate(from_tos):
#   from_tos[i] = set(from_to)

edge_cnt = [0] * (V+1)
s = [1]
visited = [False] * (V+1)
while len(s) > 0:
  idx = s.pop()
  if visited[idx]: continue

  visited[idx] = True
  edge_cnt[idx] += len(from_tos[idx])
  s.extend(from_tos[idx])

odd_edge_dot_cnt = 0
for cnt in edge_cnt:
  if cnt % 2 == 1:
    odd_edge_dot_cnt += 1

all_visited = True
for v in visited[1:]:
  all_visited &= v

if (odd_edge_dot_cnt == 2 or odd_edge_dot_cnt == 0) and all_visited:
  print("YES")
else:
  print("NO")