from collections import deque
import sys

def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

# 이 문제는 숫자들의 관계 (역/정방향)을 구하고
# 역방향일때 다음과 같은 규칙으로 구할 수 있다.

# 54 -
# 43 -
# 23 +
# 21 -

# 52413
# 15243 (-> 12)
# 15234 (-> 34)
# 12345 (-> 45)

# 98 -
# 87 -
# 67 +
# 65 -
# 54 -
# 34 +
# 23 +
# 21 -

# 12 -> 78 -> 89 -> 45 -> 56, 76 -> 67 -> 78 -> 89
# [-1, +2, -2, +1, -2]
# 양수 중 가장 큰 +2을 빼고 나머지 다 더함.

def get_num2idx(nums):
  num2idx = [-1]*(len(nums)+1)
  
  for i, num in enumerate(nums):
    num2idx[num] = i
    
  return num2idx

def get_cnts(num2idx, N):
  cnts = [0]
  
  for num in range(1,N):
    nxt_num = num+1
    
    if num2idx[num] < num2idx[nxt_num]: 
      # 정방향
      if cnts[-1] >= 0:
        cnts[-1] += 1
      else:
        cnts.append(1)
    else:
      # 역방향
      if cnts[-1] <= 0:
        cnts[-1] -= 1
      else:
        cnts.append(-1)
        
  return cnts
      
N = input(int)
nums = input_n(int)

num2idx = get_num2idx(nums)
cnts = get_cnts(num2idx, N)

print(sum(abs(cnt) for cnt in cnts) - max(0, *cnts))