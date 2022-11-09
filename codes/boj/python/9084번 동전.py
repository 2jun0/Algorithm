import sys

def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

# 1+100+1 == 1+1+100
# 항상 1+1+100 이 되게 한다.

T = input(int)

for _ in range(T):
  _ = input(int)
  coins = input_n(int)
  M = input(int)

  cnts = [0]*(M+1)
  cnts[0] = 1
  
  for coin in coins:
    for m in range(coin, M+1):
      cnts[m] += cnts[m-coin]

  print(cnts[-1])
