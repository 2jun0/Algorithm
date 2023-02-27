import sys
def input(type=str):
  return type(sys.stdin.readline().strip())
def input_n(type=str):
  return list(map(type, input().split()))

while True:
  line = input()
  if line == '#':
    break

  print(sum(line.count(aeiou) for aeiou in 'aeiouAEIOU'))
