import sys
sys.setrecursionlimit(10000000) # 재귀 제한 풀기

def input(_type=str):
	return _type(sys.stdin.readline().rstrip())
def input_n(_type):
	return list(map(_type, input().split()))

import heapq

N = input(int)
nums = []
for _ in range(N):
  heapq.heappush(nums, input(int))

result = 0
while len(nums) >= 2:
  a = heapq.heappop(nums)
  b = heapq.heappop(nums)
  result += a+b

  heapq.heappush(nums, a+b)
print(result)