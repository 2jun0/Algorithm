import sys

def input(_type=str):
  return _type(sys.stdin.readline().strip())
def input_n(_type=str):
  return list(map(_type, input().split()))

def func(a, b):
  is_prime = [True] * (int(b**0.5)+1)
  is_prime[0], is_prime[1] = False, False
  
  for x in range(2, int(b**0.5)+1):
    if is_prime[x]:
      for y in range(x+x, len(is_prime), x):
        is_prime[y] = False
  
  check = [True]*(b-a+1) # a~b로 가정함. 제곱 ㄴㄴ수 여부
  for x in range(2, len(is_prime)):
    if is_prime[x]:
      # x*x의 배수는 전부 제곱 ㄴㄴ수가 아님
      xx = x*x
      srt_X = (a // xx) * xx
      if srt_X < a:
        srt_X+=xx
      
      for X in range(srt_X, b+1, xx):
        check[X-a] = False
  cnt = 0
  for X in range(a, b+1):
    if check[X-a]:
      cnt+=1
  return cnt

a, b = input_n(int)
print(func(a,b))