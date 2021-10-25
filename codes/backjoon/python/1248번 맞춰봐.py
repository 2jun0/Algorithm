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
def avg(l): return sum(l)/len(l)
def getLRUD(i,j): return [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]

N = input(int)
L = input(str)

matrix = LL(N, N, 0)
k = 0
for i in range(N):
  for j in range(N-i):
    matrix[i][i+j] = L[k]
    k+=1

nums = [INF]*N
def check(j):
  sum_v = 0
  for i in range(j, -1, -1):
    sum_v += nums[i]

    if sum_v == 0:
      if matrix[i][j] != '0': return False
    elif sum_v < 0:
      if matrix[i][j] != '-': return False
    elif sum_v > 0:
      if matrix[i][j] != '+': return False
  return True

def func(i):
  if i == N: return True
  if matrix[i][i] == '0': 
    nums[i] = 0
    if func(i+1): return True
  else:
    for num in range(1, 11):
      nums[i] = num * (1 if matrix[i][i] == '+' else -1)
      if check(i):
        if func(i+1): return True

  return False

func(0)
print_n(nums)