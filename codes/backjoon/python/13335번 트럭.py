from collections import deque
import sys

def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
  return list(map(_type, input().split()))

n, w, L = input_n(int)
A = [0]+input_n(int)

bridge_sum = 0
bridge_q = deque([0]*w)
cnt_truck = 0
idx = 1
time = 0

while idx < len(A) or bridge_sum > 0:
  v = bridge_q.popleft()
  if v:
    bridge_sum -= v
    cnt_truck -= 1

  if idx < len(A) and bridge_sum+A[idx] <= L and cnt_truck+1 <= w:
    bridge_q.append(A[idx])
    bridge_sum+=A[idx]
    cnt_truck+=1
    idx+=1
  else:
    bridge_q.append(0)

  time += 1

print(time)