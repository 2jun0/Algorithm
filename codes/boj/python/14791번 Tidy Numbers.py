import sys

def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

def get_digits(a):
  digits = []
  
  while a > 0:
    digits.append(a%10)
    a //= 10
    
  return digits[::-1]

def tidize(digits):
  '''tidy화'''
  nine_idx = len(digits)
  for i in range(len(digits)-2, -1, -1):
    if digits[i] > digits[i+1]:
      nine_idx = i+1
      digits[i] = digits[i]-1
  
  for i in range(nine_idx, len(digits)):
    digits[i] = 9
  
  return int(''.join(map(str, digits)))
  
T = input(int)
for t in range(T):
  a = input(int)
  digits = get_digits(a)
  tidy = tidize(digits)
  print(f'Case #{t+1}: {tidy}')