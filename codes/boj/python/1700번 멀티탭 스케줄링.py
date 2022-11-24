import sys

def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

def get_close_idx(A, x, srt_idx):
  for i in range(srt_idx, len(A)):
    if A[i] == x:
      return i
  return 10000

N, K = input_n(int)
A = input_n(int)
spaces = [0]*N
switch_cnt = 0

for i, a in enumerate(A):
  if a not in spaces:
    spaces.sort(key=lambda x: (-get_close_idx(A, x, i), x))

    if spaces[0] != 0:
      switch_cnt += 1

    spaces[0] = a
print(switch_cnt)
