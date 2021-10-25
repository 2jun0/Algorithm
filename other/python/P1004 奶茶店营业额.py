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

import heapq

S = [s*0.01 for s in input_n(int)]
K, N = input_n(int)

def get_sale(t, s):
  total = 0
  for _ in range(s):
    hr = (t//60)%24
    total += S[hr]
    t+=1
  return total

A = []
for _ in range(N):
  L = input_n()
  time_s = L[0].split(':')
  A.append(
    (int(time_s[0])*60 + int(time_s[1])
    ,int(L[1])
    ,int(L[2])))

A.sort()
ks = [0]*K

total = 0
for t, s, p in A:
  k = heapq.heappop(ks)
  max_t = max(k, t)

  heapq.heappush(ks, max_t + s)

  total += p - get_sale(t, max(0, k-t))
print('%.2f' %total)