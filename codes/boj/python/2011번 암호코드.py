import sys

def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

def is_vaild(s):
	return s.isnumeric() and s[0] != '0' and 1<=int(s)<=26

s = input(str)

cnts = [0]*(len(s)+1)
"""n개 일때 경우의 수"""
cnts[0] = 1

for idx in range(len(s)):
	# 한개
	if is_vaild(s[idx]):
		cnts[idx+1] = (cnts[idx+1]+ cnts[idx]) % 1_000_000

	# 두개
	if idx-1 >= 0 and is_vaild(s[idx-1] + s[idx]):
		cnts[idx+1] = (cnts[idx+1] + cnts[idx-1]) % 1_000_000

print(cnts[-1])