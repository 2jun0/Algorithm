import sys
sys.setrecursionlimit(10000000) # 재귀 제한 풀기
INF = 10**8
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))
def print_n(L, join_str=' '):
  for i,l in enumerate(L): print(l, end=join_str if i<len(L)-1 else '\n')

N, M = input_n(int)
A = [input() for _ in range(N)]
B = []
for a in A:
	bitmask = 0
	for c in a:
		bitmask |= (1<<(ord(c)-ord('a')))
	B.append(bitmask)

mask = 0x3FFFFFF
for _ in range(M):
	cmd, arg = input_n(str)
	if cmd == '1': mask &= ~(1<<(ord(arg)-ord('a')))
	elif cmd == '2': mask |= (1<<(ord(arg)-ord('a')))
	cnt = 0
	for b in B:
		if b&mask == b: cnt+=1
	print(cnt)