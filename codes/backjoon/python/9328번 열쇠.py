from collections import deque
import sys
INF = 10**10
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

LOWERCASE_ALPHABETS = [chr(a) for a in range(ord('a'), ord('z')+1)]
UPPERCASE_ALPHABETS = [chr(A) for A in range(ord('A'), ord('Z')+1)]

def is_lower_alphabet(a):
  return ord('a') <= ord(a) <= ord('z')

def is_upper_alphabet(a):
  return ord('A') <= ord(a) <= ord('Z')

def to_idx(a):
  if is_lower_alphabet(a): return ord(a)-ord('a')
  if is_upper_alphabet(a): return ord(a)-ord('A')

T = input(int)
for _ in range(T):
  h, w = input_n(int)
  table = [input() for _ in range(h)]
  keys = input()

  # 키를 가지고 있는가?
  # 키가 있으면 True, 없으면 False
  has_keys = [True if chr(a) in keys else False for a in range(ord('a'), ord('z')+1)]
  # 키를 기다리는 문들
  waitting_doors = [deque() for _ in range(ord('A'), ord('Z')+1)]

  visited = [[False]*w for _ in range(h)]

  s = deque()

  # 시작 지점 탐색
  # 가장 자리 탐색
  for i in range(h):
    if table[i][0] != '*':
      visited[i][0] = True
      s.append((i, 0))
    if table[i][-1] != '*': 
      visited[i][-1] = True
      s.append((i, w-1))
  for j in range(1,w-1):
    if table[0][j] != '*': 
      visited[0][j] = True
      s.append((0, j))
    if table[-1][j] != '*': 
      visited[-1][j] = True
      s.append((h-1, j))

  cnt = 0
  while len(s) > 0:
    i,j = s.popleft()

    # 문서를 찾음
    if table[i][j] == '$':
      cnt+=1
    # 열쇠인 경우
    elif is_lower_alphabet(table[i][j]):
      idx = to_idx(table[i][j])

      # 열쇠 가짐.
      has_keys[idx] = True
      # 기다리고 있는 문 열어줌. -> 다시 탐색할 수 있게 큐에 넣어줌.
      while waitting_doors[idx]:
        d_i, d_j = waitting_doors[idx].popleft()
        s.append((d_i, d_j))
    # 문인데, 열쇠가 없는 경우
    elif is_upper_alphabet(table[i][j]) and not has_keys[to_idx(table[i][j])]:
      # 대기열에 넣어 둠
      waitting_doors[to_idx(table[i][j])].append((i, j))
      continue

    for t_i, t_j in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
      # 벽이 아니고 방문 하지 않은 경우
      if 0<=t_i<h and 0<=t_j<w and table[t_i][t_j] != '*' and not visited[t_i][t_j]:
        visited[t_i][t_j] = True
        s.append((t_i, t_j))

  print(cnt)