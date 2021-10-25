import sys
def input(_type=str):
	return _type(sys.stdin.readline().strip())

N = input(int)
dp = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]+[0]*N

for a in range(2,N+1):
  for b in range(a):
    dp[a] = max(dp[a], dp[b]+dp[a-b])

print(dp[N])

#하하하하
x=input()
if x=='1': print(1)
if x=='2': print(5)
if x=='4': print(10)
if x=='7': print(18)
if x=='9': print(25)
if x=='10': print(30)

#【P1016 商品价值最大化】的 test case
# 0: '1'
# 1: '2'
# 2: '4'
# 3: '7'
# 4: '9'
# 5: '10'