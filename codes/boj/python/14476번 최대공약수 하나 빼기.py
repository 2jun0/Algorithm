import sys
import math
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

N = input(int)
A = input_n(int)

lgcd = [0]*N
rgcd = [0]*N

for i, a in enumerate(A):
  if i == 0:
    lgcd[i] = a
  else:
    lgcd[i] = math.gcd(lgcd[i-1], a)
    
for i in range(N-1, -1, -1):
  if i == N-1:
    rgcd[i] = A[i]
  else:
    rgcd[i] = math.gcd(rgcd[i+1], A[i])

def get_remain_gcd(i):
  if i == 0:
    return rgcd[i+1]
  elif i == N-1:
    return lgcd[i-1]
  else:
    return math.gcd(lgcd[i-1], rgcd[i+1])

K = -1
gcd = -1
for i in range(N):
  tgcd = get_remain_gcd(i)
  
  if gcd < tgcd and A[i] % tgcd != 0:
    gcd = tgcd
    K = A[i]
  
if gcd == -1:
  print(-1)
else:
  print(gcd, K)