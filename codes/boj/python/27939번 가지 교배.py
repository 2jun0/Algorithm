import sys

def input(type_=str):
	return type_(sys.stdin.readline().rstrip())
def input_n(type_):
	return list(map(type_, input().split()))

def p_eval(L):
  if L.count('P') > 0:
    return 'P'
  else:
    return 'W'
  
def w_eval(L):
  if L.count('W') > 0:
    return 'W'
  else:
    return 'P'

n = input(int)
S = input_n(str)
m, k = input_n(int)
A = [[S[num-1] for num in input_n(int)] for _ in range(m)]

B = []
for L in A:
  B.append(p_eval(L))
print(w_eval(B))