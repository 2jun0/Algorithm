import sys

def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

def include(a, b):
  return b[0]<=a[0] and a[1]<=b[1]

N = input(int)
M = input(int)

sbus = []
bbus = []
for idx in range(M):
  a, b = input_n(int)
  if a > b:
    sbus.append((a-N, b, idx+1))
    bbus.append((a, b+N, idx+1))
  else:
    sbus.append((a, b, idx+1))
    bbus.append((a, b, idx+1))

sbus.sort(key=lambda x: (x[1],-x[0]))
bbus.sort(key=lambda x: (x[1],-x[0]))
  
ss = []
bs = []
for idx in range(M):
  while ss:
    if include(sbus[ss[-1]], sbus[idx]):
      ss.pop()
    else:
      break
    
  while bs:
    if include(bbus[bs[-1]], bbus[idx]):
      bs.pop()
    else:
      break
  
  ss.append(idx)
  bs.append(idx)
  
cnt_of_nums = [0]*(M+1)
for idx in ss:
  cnt_of_nums[sbus[idx][-1]] += 1
for idx in bs:
  cnt_of_nums[bbus[idx][-1]] += 1

ans = []
for num, cnt in enumerate(cnt_of_nums):
  if cnt == 2:
    ans.append(num)
print(*ans)