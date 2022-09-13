MAX_NUM = 9999999
is_prime = [True]*(MAX_NUM+1)

def init_is_prime():
  is_prime[0] = False
  is_prime[1] = False
  for num in range(2,MAX_NUM+1):
    if is_prime[num]:
      for nxt_num in range(num*2, MAX_NUM, num):
        is_prime[nxt_num] = False

prime_cnt = 0
visited = [False]*(MAX_NUM+1)

def dfs(numbers, made_num, selected_idx):
  global prime_cnt

  if visited[made_num]:
    return
  
  if is_prime[made_num]:
    prime_cnt += 1
  visited[made_num] = True

  made_num *= 10
  for idx in range(len(numbers)):
    if not selected_idx[idx]:
      selected_idx[idx] = True
      dfs(numbers, made_num+numbers[idx], selected_idx)
      selected_idx[idx] = False

def solution(numbers):
  numbers = list(map(int, numbers))

  init_is_prime()

  dfs(numbers, 0, [False]*len(numbers))

  return prime_cnt