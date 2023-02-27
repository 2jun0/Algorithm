import sys

def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

def merge(A, B):
  cost = 0
  R = []
  aidx = 0
  bidx = 0
  while aidx < len(A) and bidx < len(B):
    if A[aidx] <= B[bidx]:
      # A가 더 작다
      p = aidx
      cost += max(0, p - len(R))
      R.append(A[aidx])
      aidx += 1
    else:
      # B가 더 작다
      p = len(A) + bidx
      cost += max(0, p - len(R))
      R.append(B[bidx])
      bidx += 1
      
  while aidx < len(A):
    # 남은 건 cost가 생길 수 없다.
    # p = aidx
    # cost += max(0, p - len(R))
    R.append(A[aidx])
    aidx += 1
  
  while bidx < len(B):
    # 남은 건 cost가 생길 수 없다.
    # p = len(A) + bidx
    # cost += max(0, p - len(R))
    R.append(B[bidx])
    bidx += 1
  
  return R, cost

def sort(X, left, right):
  if left == right:
    return [X[left]], 0
  
  mid = (left+right) // 2
  A, a_cost = sort(X, left, mid)
  B, b_cost = sort(X, mid+1, right)
  
  R, merge_cost = merge(A, B)
  
  return R, merge_cost + a_cost + b_cost

N = input(int)
X = input_n(int)
sorted_X, cost = sort(X, 0, N-1)
print(cost)