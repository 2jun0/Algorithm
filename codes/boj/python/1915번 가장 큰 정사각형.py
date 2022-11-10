import sys

def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

n, m = input_n(int)
table = [input(str) for _ in range(n)]

dp = [[0]*m for _ in range(n)]

for y in range(n):
  for x in range(m):
    if table[y][x] == '1':
      if y-1 >= 0 and x-1 >= 0:
        dp[y][x] = min(dp[y-1][x], dp[y-1][x-1], dp[y][x-1]) + 1
      else:
        dp[y][x] = 1

print(max(max(line) for line in dp)**2)
    