import sys
INF = 10**10
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

L, C = input_n(int)
A = input_n(str)
A.sort()

def func(idx, cnt, s, cnt_vowel, cnt_consonant):
  if A[idx] in ['a','e','i','o','u']:
    cnt_vowel += 1
  else:
    cnt_consonant += 1

  s += A[idx]
  if cnt == L:
    if cnt_vowel >= 1 and cnt_consonant >= 2:
      print(s)
    return
  
  for nxt_idx in range(idx+1, C):
    func(nxt_idx, cnt+1, s, cnt_vowel, cnt_consonant)

for idx in range(C):
  func(idx, 1, '', 0, 0)