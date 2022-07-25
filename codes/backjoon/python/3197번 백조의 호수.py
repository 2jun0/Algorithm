from collections import deque
import sys
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

# Union-Find
class UnionFindNode:
  def __init__(self):
    self.p = self
  def find(self):
    if self.p != self:
      self.p = self.p.find()
    return self.p
  def union(self, n):
    n.find().p = self.find()

R, C = input_n(int)
table = [input() for _ in range(R)]
uf_tables = [[None]*C for _ in range(R)]
Ls = []

# Ques
q_waters = deque()

# 백조 찾기
def init_Ls():
  # 0 : start L
  # 1 : end L
  for i in range(R):
    for j in range(C):
      if table[i][j] == 'L':
        Ls.append((i,j))

# 물 찾기
def init_q_waters():
  for i in range(R):
    for j in range(C):
      # 물인 경우
      if table[i][j] != 'X': 
        node = UnionFindNode()

        uf_tables[i][j] = node
        q_waters.append((i, j))

# 백조 두마리가 연결되었는지 확인
def are_swans_unioned():
  return uf_tables[Ls[0][0]][Ls[0][1]].find() == uf_tables[Ls[1][0]][Ls[1][1]].find()

# q_waters 안에 있는 물 들과 다른 물을 연결함
def union_waters():
  while q_waters:
    i, j = q_waters.popleft()

    for t_i, t_j in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
      # 물인 경우
      if 0<=t_i<R and 0<=t_j<C and uf_tables[t_i][t_j]:
        if uf_tables[i][j]:
          uf_tables[i][j].union(uf_tables[t_i][t_j])
        else:
          uf_tables[i][j] = uf_tables[t_i][t_j]

# 빙판이 녹는데 걸리는 시간
def bfs():
  visited = [[False]*C  for _ in range(R)]

  q = deque()
  q_nxt = deque()
        
  c = 0

  union_waters()
  if are_swans_unioned():
    return c

  for i in range(R):
    for j in range(C):
      # 빙판만.
      if table[i][j] != 'X': continue

      for t_i, t_j in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
        if 0<=t_i<R and 0<=t_j<C and table[t_i][t_j] != 'X':
          visited[i][j] = True
          q.append((i, j))
          break

  while q:
    while q:
      i, j = q.popleft()
      # 녹은 경우 물이 되었으니 q_waters에 넣어둠.
      q_waters.append((i, j))

      for t_i, t_j in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
        # 빙판이면서 녹지 않았어야 함.
        if 0<=t_i<R and 0<=t_j<C and table[t_i][t_j] == 'X' and not visited[t_i][t_j]:
          visited[t_i][t_j] = True
          q_nxt.append((t_i, t_j))

    c+=1
    q, q_nxt = q_nxt, q

    union_waters()
    if are_swans_unioned():
      return c

init_Ls()
init_q_waters()
print(bfs())