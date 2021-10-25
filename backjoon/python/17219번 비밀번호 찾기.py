import sys

INF = 10**8
def input(_type=str):
	return _type(sys.stdin.readline().rstrip())
def input_n(_type=str):
	return list(map(_type, input().split()))
def print_n(L):
  s = ''
  for l in L: s+='{} '.format(l)
  print(s[:-1])

N, M = input_n(int)
site2pw = {}
for _ in range(N):
  site, pw = input_n()
  site2pw[site] = pw
for _ in range(M):
  site = input()
  print(site2pw[site])