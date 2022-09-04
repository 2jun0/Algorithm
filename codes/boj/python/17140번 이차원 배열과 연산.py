import sys
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

def op_r(A, width, height):
  n_width = 0
  for y in range(height):
    num_cnts = [0]*101
    for x in range(width):
      num_cnts[A[y][x]] += 1

    # (개수, 숫자) 순으로 정렬
    arr = []
    for num in range(1, 101):
      if num_cnts[num] > 0:
        arr.append((num_cnts[num], num))

    arr.sort()
    # A에 숫자, 개수로 대입
    idx = 0
    for cnt, num in arr:
      if idx >= 100:
        break

      A[y][idx] = num
      A[y][idx+1] = cnt
      idx += 2
    
    n_width = max(n_width, idx)

    # 마지막 0
    while idx < 100:
      A[y][idx] = 0
      idx += 1
  return n_width

def op_c(A, width, height):
  n_height = 0
  for x in range(width):
    num_cnts = [0]*101
    for y in range(height):
      num_cnts[A[y][x]] += 1

    # (개수, 숫자) 순으로 정렬
    arr = []
    for num in range(1, 101):
      if num_cnts[num] > 0:
        arr.append((num_cnts[num], num))

    arr.sort()
    # A에 숫자, 개수로 대입
    idx = 0
    for cnt, num in arr:
      if idx >= 100:
        break

      A[idx][x] = num
      A[idx+1][x] = cnt
      idx += 2
    
    n_height = max(n_height, idx)

    # 마지막 0
    while idx < 100:
      A[idx][x] = 0
      idx += 1
    
  return n_height

r, c, k = input_n(int)
r, c = r-1, c-1

height = 3
width = 3
A = [[0]*100 for _ in range(100)]
for y in range(3):
  line = input_n(int)
  for x in range(3):
    A[y][x] = line[x]

# 최대 100번 
turn = 0
while turn <= 100:
  if A[r][c] == k:
    break

  if height >= width:
    width = op_r(A, width, height)
  else:
    height = op_c(A, width, height)

  turn += 1

print(-1 if turn == 101 else turn)