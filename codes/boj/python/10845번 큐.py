import sys

def input(_type=str):
	return _type(sys.stdin.readline().rstrip())
def input_n(_type):
	return list(map(_type, input().split()))

N = input(int)

q = []

for _ in range(N):
  cmds = input_n(str)
  if cmds[0] == 'push':
    arg = int(cmds[1])
    q.append(arg)
  if cmds[0] == 'pop':
    if len(q) == 0: print(-1)
    else:
      tmp = q.pop(0)
      print(tmp)
  if cmds[0] == 'size':
    print(len(q))
  if cmds[0] == 'empty':
    print(1 if len(q) == 0 else 0)
  if cmds[0] == 'front':
    if len(q) == 0: print(-1)
    else:
      print(q[0])
  if cmds[0] == 'back':
    if len(q) == 0: print(-1)
    else:
      print(q[-1])