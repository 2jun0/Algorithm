import sys

S = 0
shift_arg = [1<<arg for arg in range(0, 21)]
M = int(sys.stdin.readline())
for _ in range(M):
  cmd = sys.stdin.readline().split()
  if cmd[0] == 'all':
    S = 2097151
  elif cmd[0] == 'empty':
    S = 0
  else:
    arg = int(cmd[1])
    if cmd[0] == 'add':
      S |= shift_arg[arg]
    elif cmd[0] == 'remove':
      S &= ~shift_arg[arg]
    elif cmd[0] == 'check':
      if S & shift_arg[arg]: print(1)
      else: print(0)
    elif cmd[0] == 'toggle':
      S ^= shift_arg[arg]