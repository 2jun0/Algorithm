import sys
INF = 10**10
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))
def print_n(L, join_str=' '):
  for i,l in enumerate(L): print(l, end=join_str if i<len(L)-1 else '\n')
def LL(n,m,d=0): return [[d]*n for _ in range(m)]
def avg(l): return sum(l)/len(l)

N, S = input_n(int)
L = input_n(int)
A, B = L[:N//2], L[N//2:]

cnt=0

ADP = [0]*(5000000)
ADP[0] = 1
S_ = [0]
for a in A:
  slen = len(S_)
  for i in range(slen):
    ADP[S_[i]+a] +=1 
    S_.append(S_[i]+a)

BDP = [0]*(5000000)
BDP[0] = 1
S_ = [0]
for b in B:
  slen = len(S_)
  for i in range(slen):
    BDP[S_[i]+b] +=1
    S_.append(S_[i]+b)

for adp_i in range(-2000000, 2000001):
  if -2000000 <= S-adp_i <= 2000000:
    cnt+=BDP[S-adp_i] * ADP[adp_i]
if S == 0: cnt-=1
print(cnt)
