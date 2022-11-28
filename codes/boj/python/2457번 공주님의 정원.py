import sys

def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

def to_idx(m, d):
  m-=1
  d-=1
  return max(m*31 + d, 2*31)

N = input(int)

INF = 10**8
min_cnts = [INF]*(to_idx(12, 31) + 1)

# 초기값 부분 초기화
min_cnts[to_idx(3, 1)-1] = 0

info = []
for _ in range(N):
  sm, sd, em, ed = input_n(int)

  info.append((to_idx(sm, sd), to_idx(em, ed)))

# 시작 날짜로 정렬
info.sort()

for sidx, eidx in info:
  cnt = min_cnts[sidx-1] + 1
  for idx in range(sidx, eidx):
    min_cnts[idx] = min(min_cnts[idx], cnt)

ans = min_cnts[to_idx(11, 30)]
if ans == INF:
  print(0)
else:
  print(ans)