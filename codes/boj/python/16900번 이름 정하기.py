import sys

def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

def get_fail(s):
  fail = [0]*len(s)
  l = 0
  for r in range(1, len(s)):
    while l > 0 and s[l] != s[r]:
      l = fail[l-1]
    if s[l] == s[r]:
      l += 1
      fail[r] = l
  return fail

S, K = input_n()
K = int(K)
fail = get_fail(S)

# prefix가 충첩됨.
prefix_len = fail[-1]
# 제거 하자. (반복 문자 길이)
repeat_len = len(S) - prefix_len

print(repeat_len * K + prefix_len)
