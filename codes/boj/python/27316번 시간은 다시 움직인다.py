import sys

def input(type=str):
  return type(sys.stdin.readline().strip())
def input_n(type=str):
  return list(map(type, input().split()))

def init_tree(tree, n, left, right):
  if left == right:
    tree[n] = L[left]
    return tree[n]
  
  tree[n] = tree[n] or init_tree(tree, n*2, left, (left + right) // 2)
  tree[n] = tree[n] or init_tree(tree, n*2+1, (left + right) // 2 + 1, right)
  return tree[n]

def query(tree, n, left, right, srt, end):
  if srt <= left and right <= end:
    return tree[n]
  elif end < left or right < srt:
    return False
  else:
    return query(tree, n*2, left, (left + right) // 2, srt, end)\
      or query(tree, n*2+1, (left+right)//2+1, right, srt, end)

def check(cnt, i):
  return not query(tree, 1, 0, 200000, i + cnt, min(200000, i + 2*cnt-1))

N = input(int)
T = input_n(int)
L = [False] * 200001
for t in T:
  L[t] = True
  
tree = [False]*400002
init_tree(tree, 1, 0, 200000)

# dp는 능력을 사용했을때 적용되는 구간들을 모두 체크함
dp = [[False]*500 for _ in range(200001)]
for i in range(200001):
  if L[i]:
    break
  dp[i][0] = True
  
for i in range(200001):
  for cnt in range(1, 500):
    if dp[i][cnt-1]
    
    if check(cnt, i):
      dp[i][cnt] = True

if max(dp[-1]) == True:
  print('YES')
else:
  print('NO')