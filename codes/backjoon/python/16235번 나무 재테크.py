import sys
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

N, M, K = input_n(int)
A = [input_n(int) for _ in range(N)]
foods = [[5]*N for _ in range(N)]
trees_table = [[[] for _ in range(N)] for _ in range(N)]

for _ in range(M):
  y, x, age = input_n(int)
  y, x = y-1, x-1
  trees_table[y][x].append(age)

for _ in range(K):
  # spring
  add_food_table = [[0]*N for _ in range(N)]
  new_trees_table = [[[] for _ in range(N)] for _ in range(N)]
  for y in range(N):
    for x in range(N):
      trees_table[y][x].sort()
      for age in trees_table[y][x]:
        if foods[y][x]-age < 0:
          add_food_table[y][x] += age//2
        else:
          foods[y][x] -= age
          new_trees_table[y][x].append(age+1)
      
  trees_table = new_trees_table
  
  # summer
  for y in range(N):
    for x in range(N):
      foods[y][x] += add_food_table[y][x]

  # autumn
  for y in range(N):
    for x in range(N):
      for age in trees_table[y][x]:
        if age % 5 == 0:
          for n_y, n_x in [(y-1, x-1), (y-1, x), (y-1, x+1), (y, x-1), (y, x+1), (y+1, x-1), (y+1, x), (y+1, x+1)]:
            if 0<=n_y<N and 0<=n_x<N:
              trees_table[n_y][n_x].append(1)

  # winter
  for y in range(N):
    for x in range(N):
      foods[y][x] += A[y][x]

cnt = 0
for y in range(N):
  for x in range(N):
    cnt += len(trees_table[y][x])

print(cnt)