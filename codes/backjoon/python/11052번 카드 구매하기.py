import sys
sys.setrecursionlimit(10000000) # 재귀 제한 풀기

def input(_type=str):
	return _type(sys.stdin.readline().rstrip())
def input_n(_type):
	return list(map(_type, input().split()))

N = input(int)
P = input_n(int)
P = [0] + P

for i in range(2, N+1):
  for j in range(1, i//2+1):
    P[i] = max(P[i], P[j]+P[i-j])

print(P[N])