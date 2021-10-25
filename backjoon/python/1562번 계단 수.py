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

# [len][last_num][visitied] # 마지막 visitied는 bitmask로
DP = [[[0]*(1<<10) for _ in range(10)] for _ in range(N)]
for num in range(10): DP[0][num][1<<num] = 1
for lv in range(0,N-1):
  for last_num in range(10):
    for visitied in range(1<<10):
      if last_num < 9: DP[lv+1][last_num+1][visitied | 1<<(last_num+1)] = (DP[lv+1][last_num+1][visitied | 1<<(last_num+1)] + DP[lv][last_num][visitied])%1000000000
      if last_num > 0: DP[lv+1][last_num-1][visitied | 1<<(last_num-1)] = (DP[lv+1][last_num-1][visitied | 1<<(last_num-1)] + DP[lv][last_num][visitied])%1000000000

#print(sum([sum([DP[n][num][(1<<10)-1] for num in range(1,10)]) for n in range(40)]))
print(sum([DP[N-1][num][(1<<10)-1] for num in range(1,10)]) % 1000000000)