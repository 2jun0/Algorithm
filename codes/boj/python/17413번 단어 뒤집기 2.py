import sys

def input(_type=str):
	return _type(sys.stdin.readline().rstrip())
def input_n(_type):
	return list(map(_type, input().split()))

S = input()
S1 = ''
i = 0
s_i = 0
def swap_save():
  global S1
  S1 += S[s_i:i][::-1]
while i < len(S):
  if S[i] == ' ':
    swap_save()
    S1 += S[i]
    i+=1
    s_i=i
    continue
  if S[i] == '<':
    swap_save()
    S1 += S[i]
    i+=1
    while S[i] != '>': 
      S1 += S[i]
      i+=1
    S1 += S[i]
    i+=1
    s_i=i
    continue
  i+=1
swap_save()
print(S1)