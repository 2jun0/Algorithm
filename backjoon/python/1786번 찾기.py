import sys
sys.setrecursionlimit(10000000) # 재귀 제한 풀기
INF = 10**8
def input(_type=str):
	return _type(sys.stdin.readline()[:-1])
def input_n(_type=str):
	return list(map(_type, input().split()))
def print_n(L):
  s = ''
  for l in L: s+='{} '.format(l)
  print(s[:-1])

T = input()
P = input()

pi = [0]*len(P)
j = 0
for i in range(1,len(P)):
  while j>0 and P[i] != P[j]: j = pi[j-1]
  if P[i] == P[j]:
    j+=1
    pi[i] = j

j = 0
match = []
for i in range(len(T)):
  while j>0 and (j==len(P) or T[i] != P[j]):
    j = pi[j-1]
  if T[i] == P[j]:
    j+=1
    if j == len(P): match.append(i-j+2)
print(len(match))
print_n(match)