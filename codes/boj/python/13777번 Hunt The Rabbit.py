import sys
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

def find_num(num):
  start = 1
  end = 50
  log = []

  while start <= end:
    mid = (start + end) // 2
    log.append(mid)

    if num == mid:
      break
    elif num < mid:
      end = mid - 1
    else:
      start = mid + 1
  return log

while True:
  num = input(int)
  if num == 0:
    break

  print(' '.join(map(str, find_num(num))))
