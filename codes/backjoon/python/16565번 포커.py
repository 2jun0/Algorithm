import sys
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

LIMIT = 10007

def combination(n,m):
  def factorial(_x):
    result = 1
    for x in range(1, _x+1):
      result = (result*x) % LIMIT
    return result
  
  def divide(a, b):
    def power(x, p): # x ^ p
      if p == 0: return 1 # x ^ 0 == 1
      t = power(x, p // 2)
      if p % 2 == 1: # x^p = t*t*x
        return (t*t * x) % LIMIT
      else: # x^p = t*t
        return (t*t) % LIMIT

    return (a * power(b, LIMIT-2)) % LIMIT

  return divide(factorial(n), (factorial(m) * factorial(n-m))) % LIMIT

N = input(int)
# N(A1) = 13C1 * (52-4)C(N-4) 1세트 이상 뽑은 경우
# N(A1) - A(A2) = N(A1) + N(A2) - N(A1 + A2) = 13C1 * (52-4)C(N-4) - 13C2 * (52-8)C(N-8)

# And, N(dp(lv)) = 13Clv * (52-lv*4)C(N-lv*4)
# 0 < lv <= 13 (dp0 = 0)

# N(A1) = dp(1)
# N(A1 U A2) = dp(1) - dp(2)
# N(A1 U A2 U A3) = dp(1) - dp(2) + dp(3)

# So, N(A1 U A2 ..... U An) = dp(1) - dp(2) + dp(3) ..... (-1)^(n-1) dp(n)

cnt_of_sets = N//4

dp = [0] + [
  (combination(13,lv) * combination(52-lv*4,N-lv*4)) % LIMIT 
    for lv in range(1,cnt_of_sets+1)]

sum_of_sets = 0
for lv in range(1,cnt_of_sets+1):
  sum_of_sets += (-1)**(lv-1) * dp[lv] % LIMIT

sum_of_sets %= LIMIT

print(sum_of_sets)

## 풀었지만... 공식을 제대로 쓰지 못함..