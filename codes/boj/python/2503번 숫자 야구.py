import sys

def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

def get_strike(A, B):
  cnt = 0
  for a, b in zip(A, B):
    if a == b:
      cnt += 1
    
  return cnt 

def get_ball(A, B):
  cnt = 0
  for a in A:
    if a in B:
      cnt += 1
  return cnt - get_strike(A, B)

def match(infos, B):
  for A, s, b in infos:
    A = str(A)
    if s != get_strike(A, B) or b != get_ball(A, B):
      return False
  
  return True

T = input(int)

infos = [input_n(int) for _ in range(T)]

cnt = 0
for t1 in range(1, 10):
  for t2 in range(1, 10):
    for t3 in range(1, 10):
      if t1 == t2 or t1 == t3 or t2 == t3:
        continue
      
      nums = str(t1)+str(t2)+str(t3)
      if match(infos, nums):
        cnt += 1
        
print(cnt)