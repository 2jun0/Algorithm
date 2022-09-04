import sys
def input(_type=str):
	return _type(sys.stdin.readline().rstrip())
def input_n(_type=str):
	return list(map(_type, input().split()))

N, M = input_n(int)
table = [input_n(int) for _ in range(N)]

tetrominos = [
  # ㅁㅁㅁㅁ
  [(0,0), (1,0), (2,0), (3,0)],
  [(0,0), (0,1), (0,2), (0,3)],
  # ㅁㅁ 
  # ㅁㅁ
  [(0,0), (0,1), (1,0), (1,1)],
  # ㅁㅁㅁ  ㅁㅁㅁ ㅁ        ㅁ
  # ㅁ         ㅁ ㅁㅁㅁ ㅁㅁㅁ
  [(0,0), (1,0), (2,0), (0,1)],
  [(0,0), (1,0), (2,0), (2,1)],
  [(0,0), (0,1), (1,1), (2,1)],
  [(2,0), (0,1), (1,1), (2,1)],
  # ㅁㅁ   ㅁㅁ  ㅁ      ㅁ
  # ㅁ       ㅁ  ㅁ      ㅁ
  # ㅁ       ㅁ  ㅁㅁ  ㅁㅁ
  [(0,0), (1,0), (0,1), (0,2)],
  [(0,0), (1,0), (1,1), (1,2)],
  [(0,0), (0,1), (0,2), (1,2)],
  [(1,0), (1,1), (0,2), (1,2)],
  # ㅁ      ㅁ  ㅁㅁ      ㅁㅁ
  # ㅁㅁ  ㅁㅁ    ㅁㅁ  ㅁㅁ
  #   ㅁ  ㅁ
  [(0,0), (0,1), (1,1), (1,2)],
  [(1,0), (0,1), (1,1), (0,2)],
  [(0,0), (1,0), (1,1), (2,1)],
  [(1,0), (2,0), (0,1), (1,1)],
  # ㅁㅁㅁ   ㅁ    ㅁ      ㅁ
  #   ㅁ   ㅁㅁㅁ  ㅁㅁ  ㅁㅁ
  #               ㅁ      ㅁ
  [(0,0), (1,0), (2,0), (1,1)],
  [(1,0), (0,1), (1,1), (2,1)],
  [(0,0), (0,1), (1,1), (0,2)],
  [(1,0), (0,1), (1,1), (1,2)]
]

def ok_b(i, j):
  return 0<=i<N and 0<=j<M

def get_t(i, j, tetromino):
  sum = 0
  for a,b in tetromino:
    if not ok_b(i+a, j+b): return -1
    else: sum+=table[i+a][j+b]
  return sum

max_v = 0
for t in tetrominos:
  for i in range(N):
    for j in range(M):
      max_v = max(max_v, get_t(i,j,t))
print(max_v)