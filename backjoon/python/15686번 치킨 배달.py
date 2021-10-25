import sys
sys.setrecursionlimit(10000000) # 재귀 제한 풀기

def _input(_type=str):
	return _type(sys.stdin.readline().rstrip())
def _input_n(_type):
	return list(map(_type, _input().split()))

N, M = _input_n(int)
G = [_input_n(int) for _ in range(N)]

cs = []
hs = []

for i, l in enumerate(G):
  for j, g in enumerate(l):
    if g == 1:
      hs.append((i,j))
    elif g == 2:
      cs.append((i,j))

dists = []

for c in cs:
  l = []
  for h in hs:
    l.append(abs(c[0]-h[0]) + abs(c[1]-h[1]))
  dists.append(l)

sum_min_dist = 999999999
# idx, include, recent_min_dists
s = []
s.append((0, True, [99999]*len(hs)))
cnt = 0

while len(s) > 0:
  idx, include, recent_min_dists = s.pop()

  if include:
    # 하나 추가
    cnt += 1

    current_min_dists = []
    for recent, this in zip(recent_min_dists, dists[idx]):
      current_min_dists.append(this if recent>this else recent)

    sum_min_dist = min(sum_min_dist, sum(current_min_dists))

    s.append((idx, False, recent_min_dists))
    if cnt < M and idx+1 < len(dists): s.append((idx+1, True, current_min_dists))
  else:
    # 하나 삭제
    cnt -= 1
    if cnt < M and idx+1 < len(dists): s.append((idx+1, True, recent_min_dists))

print(sum_min_dist)