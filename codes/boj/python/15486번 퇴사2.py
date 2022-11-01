import sys
def input(_type=str):
	return _type(sys.stdin.readline().rstrip())
def input_n(_type):
	return list(map(_type, input().split()))

N = input(int)
prices = [0]*(N+1)

for day in range(N):
  t, p = input_n(int)

  if day-1 >= 0:
    prices[day] = max(prices[day], prices[day-1])

  if day+t < N+1:
    prices[day+t] = max(prices[day+t], prices[day]+p)

print(max(prices))