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

N, M = input_n(int)
table = [input() for _ in range(N)]
K = input(int)
l_cnt = {}

for l in table:
  if l in l_cnt.keys():l_cnt[l]+=1
  else: l_cnt[l]=1

max_cnt = 0
for l, cnt in l_cnt.items():
  False_cnt = 0
  for c in l:
    if c=='0': False_cnt += 1
  
  if False_cnt % 2 == K % 2 and False_cnt <= K:
    max_cnt = max(max_cnt, cnt)

print(max_cnt)