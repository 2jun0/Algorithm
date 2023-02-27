import sys
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

# 그냥 구하면 5000C4 => 너무 큼
# 쪼개면 줄어든다. 5000C2 * 2 => 3천만 정도

# a+b+c+d = w

w, n = input_n(int)
A = input_n(int)

AB = [None]*(800000)

# a+b
for a_idx in range(n):
  for b_idx in range(a_idx+1, n):
    AB[A[a_idx] + A[b_idx]] = (a_idx, b_idx)

flag = False
for c_idx in range(n):
  for d_idx in range(c_idx+1, n):
    if w-A[c_idx]-A[d_idx] >= 0 and AB[w-A[c_idx]-A[d_idx]] and (c_idx not in AB[w-A[c_idx]-A[d_idx]] and d_idx not in AB[w-A[c_idx]-A[d_idx]]):
      flag = True
      break

print('YES' if flag else 'NO')