import sys
sys.setrecursionlimit(10000000) # 재귀 제한 풀기
INF = 10**10
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))
def print_n(L, join_str=' '):
  for i,l in enumerate(L): print(l, end=join_str if i<len(L)-1 else '\n')
def LL(n,m,d=0): return [[d]*n for _ in range(m)]

a, b, c =input_n(int)
m = 0
if a == b and b == c: m = 10000+a*1000
elif a == b and b != c: m = 1000+a*100
elif a == c and a != b: m = 1000+a*100
elif c == b and c != a: m = 1000+c*100
elif c != b and c != a and a != b: m = max(a,b,c)*100
print(m)