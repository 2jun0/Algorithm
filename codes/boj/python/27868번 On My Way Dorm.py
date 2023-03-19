import sys
sys.setrecursionlimit(200002)

def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))  

input()
input()
cmds = input()
print(cmds[::-1])