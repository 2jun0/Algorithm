import sys
INF = 10**10
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))
def print_n(L, join_str=' '):
  for i,l in enumerate(L): print(l, end=join_str if i<len(L)-1 else '\n')
def LL(n,m,d=0): return [[d]*m for _ in range(n)]
def avg(l): return sum(l)/len(l)
def getLRUD(i,j): return [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]

N = input(int)
A = [input() for _ in range(N)]
D = [[0, chr(i)] for i in range (ord('A'), ord('J') + 1)]
dont_zero = []

for a_i, a in enumerate(A):
  dont_zero.append(a[0])
  for e_i, e in enumerate(a):
    d_i = ord(e) - ord('A')
    D[d_i][0] += 10**(len(a) - e_i - 1)
dont_zero = list(set(dont_zero))

D.sort()
sum = 0
num_s = [i for i in range(10)]
for d, e in D:
  if num_s[0] == 0 and e in dont_zero:
    sum += d * num_s[1]
    del num_s[1]
  else:
    sum += d * num_s[0]
    del num_s[0]
  
print(sum)
