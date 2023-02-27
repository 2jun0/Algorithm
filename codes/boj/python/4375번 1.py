import sys
for line in sys.stdin.readlines():
  n = int(line)
  x = 1
  p = 1

  while x % n != 0:
    x = x * 10 + 1
    p+=1
  print(p)
  