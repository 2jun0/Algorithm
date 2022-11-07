import sys
def input(_type=str):
	return _type(sys.stdin.readline().rstrip())
def input_n(_type):
	return list(map(_type, input().split()))

'''
1+2+1 == 1+1+2 같은 중복 문제를 해결하고자 한다면,
순서를 정해두면 된다.
-> 1+1+2
'''

n, k = input_n(int)
coins = []

for _ in range(n):
  coins.append(input(int))

cases_by_sum = [0]*(k+1)
cases_by_sum[0] = 1

for coin in coins:
  for sum_v in range(1, k+1):
    if sum_v - coin >= 0:
      cases_by_sum[sum_v] += cases_by_sum[sum_v - coin]

print(cases_by_sum[-1])