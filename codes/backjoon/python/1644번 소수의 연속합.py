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

N = input(int)

isPrime = [True]*(N+1)
isPrime[0], isPrime[1] = False, False
for num in range(2, N+1):
  if isPrime[num]:
    for num2 in range(num*2, N+1, num): isPrime[num2] = False
P = []
for num in range(2,N+1):
  if isPrime[num]:
    P.append(num)

left = 0
right = 0
if N == 1: sum_val = 0
else: sum_val = P[0]
cnt = 0
while True:
  if sum_val == N: cnt+=1

  if sum_val >= N and left+1 <= right:
    sum_val -= P[left]
    left += 1
  elif sum_val < N and right+1 < len(P):
    right += 1
    sum_val += P[right]
  else:
    break
print(cnt)