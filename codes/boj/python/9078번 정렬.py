import sys

def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

T = input(int)
for _ in range(T):
  N = input(int)
  A = input_n(int)
  
  cnt = 0
  for i in range(N):
    for j in range(i+1, N):
      if A[i] > A[j]:
        cnt += 1
      
  if cnt %2 == 0:
    print('YES')
  else:
    print('NO')