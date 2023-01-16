import sys
from collections import deque
def input(_type=str):
  return _type(sys.stdin.readline().strip())
def input_n(_type=str):
  return list(map(_type, input().split()))

N, M, C = input_n(int)
W = [input_n(int) for _ in range(C)]
A = input_n(int)
B = input_n(int)

prev_dp = [0]*(M+1)
curr_dp = [0]*(M+1)

for a in A:
  for bi, b in enumerate(B):
    curr_dp[bi+1] = max(prev_dp[bi+1], prev_dp[bi] + W[a-1][b-1], curr_dp[bi])
  curr_dp, prev_dp = prev_dp, curr_dp
  
print(prev_dp[-1])  
#       [0,00,00,00,00]
# 1   2 [0,01,10,10,10]
# 1   1 [0,01,11,20,20]
# 1   1 [0,01,11,21,30]
# 2   1 [0,20,20,20,30]

# 10 1
# 1 20

# 1   1 [0,1,10,10]
# 2   2 [0,10,11,20]
#     2

# 하나의 A -> 모든 B와 악수 M번
# 모든 A -> 모든 B와 악수 N*M번
# 1,000,000 -> 해볼만 하다.

# M*(M-1)*(M-2) .... = M!